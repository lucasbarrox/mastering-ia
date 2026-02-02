import os
import streamlit as st
import numpy as np
from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="ChatPDF Pro", page_icon="📚")
st.title("📚 Chat com seus Documentos (RAG)")

# 2. CARREGAR CHAVES E API
# Carrega do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API Key não encontrada. Configure o .env")
    st.stop()

# Cache Resource: Carrega o cliente só uma vez para não ficar lento
@st.cache_resource
def get_client():
    return genai.Client(api_key=api_key)

client = get_client()

# 3. GESTÃO DE ESTADO (MEMÓRIA)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Começa vazio

if "db_vetorial" not in st.session_state:
    st.session_state.db_vetorial = None # Começa sem documento

# 4. FUNÇÕES DE BACK-END (RAG)
def processar_pdf(uploaded_file):
    """Lê o PDF e cria os vetores (Embeddings)"""
    reader = PdfReader(uploaded_file)
    texto_completo = ""
    for page in reader.pages:
        texto_completo += page.extract_text() + "\n"
    
    # Quebrando em pedaços (Chunks) de ~500 caracteres
    chunks = [c.strip() for c in texto_completo.split('\n\n') if len(c) > 50]
    
    # Criando Embeddings
    database = []
    status_bar = st.progress(0, text="Processando Inteligência...")
    
    for i, chunk in enumerate(chunks):
        # Chama a API de Embeddings (text-embedding-004)
        resp = client.models.embed_content(
            model="text-embedding-004",
            contents=chunk
        )
        vetor = np.array(resp.embeddings[0].values)
        database.append({"texto": chunk, "vetor": vetor})
        
        # Atualiza barra de progresso
        status_bar.progress((i + 1) / len(chunks))
        
    status_bar.empty() # Some com a barra quando acabar
    return database

def buscar_resposta(pergunta, db):
    """Acha o melhor trecho e gera a resposta"""
    # 1. Vetoriza a pergunta
    resp = client.models.embed_content(model="text-embedding-004", contents=pergunta)
    vetor_pergunta = np.array(resp.embeddings[0].values)
    
    # 2. Busca (Dot Product)
    melhor_score = -1
    melhor_texto = ""
    
    for item in db:
        score = np.dot(item["vetor"], vetor_pergunta)
        if score > melhor_score:
            melhor_score = score
            melhor_texto = item["texto"]
    
    # 3. Gera Resposta com Gemini 2.5
    prompt = f"""
    Use o contexto abaixo para responder a pergunta. Se não souber, diga que não sabe.
    CONTEXTO: {melhor_texto}
    PERGUNTA: {pergunta}
    """
    
    resp_gen = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return resp_gen.text, melhor_texto

# 5. FRONT-END (BARRA LATERAL DE UPLOAD)
with st.sidebar:
    st.header("Upload")
    uploaded_file = st.file_uploader("Suba seu PDF aqui", type="pdf")
    
    if uploaded_file and st.session_state.db_vetorial is None:
        with st.spinner("Lendo e Vetorizando..."):
            db = processar_pdf(uploaded_file)
            st.session_state.db_vetorial = db # Salva na memória persistente
            st.success("PDF Processado! Pode perguntar.")

    if st.button("Limpar Conversa"):
        st.session_state.chat_history = []
        st.rerun() # Recarrega a página

# 6. FRONT-END (CHAT PRINCIPAL)
# Exibe mensagens antigas
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Caixa de entrada do usuário
if prompt := st.chat_input("Pergunte sobre o documento..."):
    # 1. Mostra pergunta do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # 2. Verifica se tem PDF carregado
    if st.session_state.db_vetorial is None:
        response = "Por favor, faça upload de um PDF primeiro na barra lateral."
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
    else:
        # 3. Processa a resposta (RAG)
        resposta_ia, fonte = buscar_resposta(prompt, st.session_state.db_vetorial)
        
        # Formata a resposta mostrando a fonte (opcional)
        resposta_final = f"{resposta_ia}\n\n*Fonte encontrada: {fonte[:100]}...*"
        
        with st.chat_message("assistant"):
            st.markdown(resposta_final)
        st.session_state.chat_history.append({"role": "assistant", "content": resposta_final})