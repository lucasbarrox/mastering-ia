import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# sempre gerar os mesmos números
np.random.seed(42)

# Gerar 50 clientes
n_samples = 50

# Renda aleatória entre R$ 1000 e R$ 10.000
X_renda = np.random.randint(1000, 10000, n_samples)

# FÓRMULA
# y = w * x + b + ruído
# Peso (w) = 0.05
# Bias (b) = 150
ruido = np.random.normal(0, 50, n_samples) 

y_score = (0.05 * X_renda) + 150 + ruido

# Salvar
df = pd.DataFrame({'Renda': X_renda, 'Score': y_score})
df.to_csv('dados_credito.csv', index=False)

print("--- Dados Gerados ---")
print(df.head())

# Visualizar a dispersão (Para provar que parece uma reta)
plt.scatter(df['Renda'], df['Score'], color='blue', alpha=0.5)
plt.title('Renda vs Score (Com Ruído)')
plt.xlabel('Renda (R$)')
plt.ylabel('Score (Pontos)')
plt.savefig('dispersao_dados.png')
print("Gráfico 'dispersao_dados.png' salvo.")