import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Carregar segurança
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERRO: Chave não encontrada. Verifique o .env")
    exit()

# 2. Configurar o Cliente
client = genai.Client(api_key=api_key)

# 3. Personalidade "Marcus"
system_instruction = """
Você é um Tech Recruiter Sênior do Vale do Silício, famoso por ser brutalmente honesto, 
mas extremamente eficaz. Seu nome é 'Marcus'.

Seu trabalho é analisar a apresentação de candidatos e dizer:
1. O que está ruim (sem massagem).
2. O que precisa melhorar para ganhar salários acima de $100k/ano.
3. Use gírias corporativas como 'Hard Skills', 'Culture Fit', 'Red Flag'.
"""

# 4. Iniciando o Chat (Usando Gemini 2.5 Flash)
print("--- 👔 Chat com Marcus (Tech Recruiter - Powered by Gemini 2.5) ---")
print("Marcus: Mande seu resumo. Estou sem tempo.")

try:
    chat = client.chats.create(
        model="gemini-2.5-flash", 
        config=types.GenerateContentConfig(
            temperature=0.4,
            max_output_tokens=1000,
            system_instruction=system_instruction
        )
    )

    # 5. Loop de Conversa
    while True:
        user_input = input("\nVocê: ")
        
        if user_input.lower() in ["sair", "exit", "tchau"]:
            print("Marcus: Finalmente. Vá estudar.")
            break
        
        print("Marcus está analisando...")
        
        response = chat.send_message(user_input)
        print(f"Marcus: {response.text}")

except Exception as e:
    print(f"❌ Erro crítico: {e}")