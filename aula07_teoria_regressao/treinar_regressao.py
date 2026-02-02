import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("--- 🕵️‍♀️ Investigação Matemática com IA ---")

# Carregar dados
df = pd.read_csv('dados_credito.csv')
X = df[['Renda']] 
y = df['Score']   

# Treinar (O computador vai calcular os Mínimos Quadrados)
modelo = LinearRegression()
modelo.fit(X, y)

# Scikit-Learn guarda o 'w' em .coef_ e o 'b' em .intercept_
coeficiente_w = modelo.coef_[0]
intercepto_b = modelo.intercept_

print(f"\nMatemática Descoberta pela IA:")
print(f"Intercepto (b) encontrado: {intercepto_b:.4f} (Real era 150)")
print(f"Peso da Renda (w) encontrado: {coeficiente_w:.4f} (Real era 0.05)")

print("\n--- Conclusão Teórica ---")
print(f"A equação da reta encontrada é: Score = {coeficiente_w:.4f} * Renda + {intercepto_b:.4f}")

# Prova real
renda_teste = 5000
previsao_ia = modelo.predict([[renda_teste]])[0]

# Cálculo manual usando a fórmula que a IA achou
calculo_manual = (coeficiente_w * renda_teste) + intercepto_b

print(f"\n--- Teste com Renda de R$ {renda_teste} ---")
print(f"Previsão da função .predict(): {previsao_ia:.4f}")
print(f"Cálculo Manual (w*x + b):      {calculo_manual:.4f}")

# Reta de regressão
# Plot dos pontos originais e a reta que a IA traçou
plt.figure(figsize=(10, 6))
plt.scatter(df['Renda'], df['Score'], color='blue', label='Dados Reais (Com Ruído)')
plt.plot(df['Renda'], modelo.predict(df[['Renda']]), color='red', linewidth=2, label='Reta de Regressão (IA)')
plt.title(f'Regressão Linear: y = {coeficiente_w:.2f}x + {intercepto_b:.2f}')
plt.xlabel('Renda')
plt.ylabel('Score')
plt.legend()
plt.savefig('reta_final.png')
print("\nGráfico 'reta_final.png' salvo.")