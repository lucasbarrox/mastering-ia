import pandas as pd
import numpy as np

print("--- 🧹 Iniciando Pipeline de Limpeza ---")

# CARREGAMENTO
# O parâmetro 'na_values' ajuda a identificar textos que significam vazio
try:
    df = pd.read_csv("dados_brutos.csv")
    print("Arquivo carregado. Amostra inicial:")
    print(df)
except FileNotFoundError:
    print("ERRO: Gere o CSV primeiro!")
    exit()

print("\n--- 🔍 Análise de Problemas ---")
print(df.info()) # Mostra tipos de dados e contagem de nulos
print("\nValores Nulos por Coluna:")
print(df.isnull().sum())

# LIMPEZA (Data Cleaning)

# Removendo linhas onde o NOME é vazio (sem nome não dá pra cadastrar)
# axis=0 remove linhas, how='any' remove se tiver qualquer Nulo na coluna especificada
df = df.dropna(subset=['nome'])

# Corrigindo a coluna RENDA (está como texto por causa do "ERROR")
# Passo 1: Forçar erro virar NaN (Not a Number)
df['renda_mensal'] = pd.to_numeric(df['renda_mensal'], errors='coerce')

# Passo 2: Preencher a renda que falta com a MÉDIA das outras rendas
media_renda = df['renda_mensal'].mean()
df['renda_mensal'] = df['renda_mensal'].fillna(media_renda)

# Corrigindo a IDADE (Preencher com a MEDIANA para evitar distorções)
mediana_idade = df['idade'].median()
df['idade'] = df['idade'].fillna(mediana_idade)

# Corrigindo SCORE (Vamos assumir média aqui)
df['score_credito'] = df['score_credito'].fillna(df['score_credito'].mean())

print("\n--- ✨ Dados Limpos ---")
print(df)

# SALVAMENTO
df.to_csv("dados_limpos.csv", index=False)
print("\n✅ Arquivo 'dados_limpos.csv' salvo com sucesso!")