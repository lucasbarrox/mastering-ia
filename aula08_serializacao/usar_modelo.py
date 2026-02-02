import joblib
import pandas as pd

print("--- 📱 Fase 2: Aplicação (Produção) ---")

# Carregar o modelo salvo
try:
    ia_carregada = joblib.load('modelo_credito_v1.pkl')
    print("✅ Cérebro carregado da memória!")
except FileNotFoundError:
    print("❌ Erro: Arquivo .pkl não encontrado. Rode o script de treino antes.")
    exit()

# Interação com o usuário
print("\n--- Sistema de Aprovação de Crédito ---")
renda_usuario = float(input("Digite a renda do cliente: R$ "))

# Prever o score usando o modelo carregado
dados_novos = pd.DataFrame({'Renda': [renda_usuario]})

score_previsto = ia_carregada.predict(dados_novos)[0]

print(f"\n🔮 Previsão para Renda R$ {renda_usuario:.2f}:")
print(f"Score Estimado: {score_previsto:.0f} pontos")

# Regra de Negócio simples
if score_previsto > 400:
    print("Resultado: APROVADO ✅")
else:
    print("Resultado: REPROVADO ❌")