import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

print("--- 🏭 Fase 1: Fábrica de Modelos ---")

# Gerar dados sintéticos
np.random.seed(42)
X_renda = np.random.randint(1000, 10000, 100)
ruido = np.random.normal(0, 50, 100)
y_score = (0.05 * X_renda) + 150 + ruido

# Organizando em DataFrame
df = pd.DataFrame({'Renda': X_renda, 'Score': y_score})

# Treinar
model = LinearRegression()
model.fit(df[['Renda']], df['Score'])

print(f"Modelo treinado! Coeficiente: {model.coef_[0]:.4f}")

# SERIALIZAÇÃO (Salvando o cérebro)
# dump(objeto_para_salvar, 'nome_do_arquivo.pkl')
nome_arquivo = 'modelo_credito_v1.pkl'
joblib.dump(model, nome_arquivo)

print(f"\n✅ SUCESSO! Modelo salvo em '{nome_arquivo}'.")
print("Modelo pronto para ser usado em produção!")