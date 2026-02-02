import os
import numpy as np
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("--- 🧠 Inicializando Sistema RAG (Neural Search) ---")



# Carregar o texto do arquivo
with open("manual_produto_x.txt", "r") as f:
    texto_completo = f.read()

# Dividir o texto em chunks menores

chunks = [linha.strip() for linha in texto_completo.split('\n') if linha.strip()]

print(f"📚 Documento carregado. {len(chunks)} fragmentos de informação encontrados.")

# Criar embeddings para cada chunk

print("🧮 Calculando vetores matemáticos para cada frase...")

def get_embedding(text):
    # Chama a API do Google para vetorizar o texto
    result = client.models.embed_content(
        model="text-embedding-004",
        contents=text
    )
    return result.embeddings[0].values

# Criamos um "Banco de Dados Vetorial" na memória RAM
# database_vetorial = [ (texto_original, vetor_matematico), ... ]
database_vetorial = []
for chunk in chunks:
    vetor = get_embedding(chunk)
    database_vetorial.append({
        "texto": chunk,
        "vetor": np.array(vetor) # Convertendo para NumPy para fazer contas
    })

print("✅ Indexação concluída! O sistema aprendeu o documento.")

# FUNÇÃO DE BUSCA DO MELHOR CONTEXTO
def buscar_melhor_contexto(pergunta):
    # A) Vetoriza a pergunta do usuário
    vetor_pergunta = np.array(get_embedding(pergunta))
    
    melhor_score = -1
    melhor_texto = ""
    
    # B) Compara a pergunta com cada pedaço do documento (Produto Escalar)
    for item in database_vetorial:
        # Cálculo de Similaridade de Cosseno simplificado (Dot Product)
        score = np.dot(item["vetor"], vetor_pergunta)
        
        if score > melhor_score:
            melhor_score = score
            melhor_texto = item["texto"]
            
    return melhor_texto, melhor_score

# LOOP DE INTERAÇÃO COM O USUÁRIO
print("\n--- 💬 Pergunte sobre o X-2000 (Digite 'sair' para fechar) ---")

while True:
    pergunta = input("\nSua dúvida: ")
    if pergunta.lower() in ["sair", "exit"]: break
    
    # RETRIEVAL (Buscar o melhor contexto no doc)
    contexto, score = buscar_melhor_contexto(pergunta)
    
    print(f"   🕵️  Fato encontrado no doc (Similaridade: {score:.4f}):")
    print(f"   > '{contexto}'")
    
    if score < 0.65: # Se a similaridade for baixa, talvez o doc não tenha a resposta
        print("   ⚠️  Aviso: Não tenho certeza se o documento fala sobre isso.")

    # GENERATION (A IA responde usando o contexto)
    prompt_final = f"""
    Você é um assistente técnico útil. Responda à pergunta do usuário usando APENAS o contexto abaixo.
    Se a resposta não estiver no contexto, diga "Não sei informar com base no manual".
    
    CONTEXTO: {contexto}
    
    PERGUNTA: {pergunta}
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_final
    )
    
    print(f"\n🤖 Resposta da IA: {response.text}")