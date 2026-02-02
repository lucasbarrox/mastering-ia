import torch
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

print("--- 🌀 Gerando Dados Não-Lineares ---")

# Gerar dados usando make_circles
# factor=0.5: O círculo de dentro é metade do tamanho do de fora 
# noise=0.03: Um pouco de bagunça para não ficar perfeito demais
X, y = make_circles(n_samples=1000, noise=0.03, random_state=42, factor=0.5)

# Visualizar
plt.figure(figsize=(8, 6))
# Plotar pontos onde y=0 (Círculo de fora) em Azul
plt.scatter(X[y==0, 0], X[y==0, 1], c='blue', label='Classe 0 (Fora)')
# Plotar pontos onde y=1 (Círculo de dentro) em Vermelho
plt.scatter(X[y==1, 0], X[y==1, 1], c='red', label='Classe 1 (Dentro)')
plt.legend()
plt.title("O Problema dos Círculos (Impossível para Regressão Linear)")
plt.savefig("dados_circulos.png")

print("✅ Gráfico salvo em 'dados_circulos.png'. Abra e tente imaginar uma reta separando as cores.")

# Convertendo para Tensores PyTorch
# X: features, y: labels
X_tensor = torch.from_numpy(X).type(torch.float)
y_tensor = torch.from_numpy(y).type(torch.float)

# Salvar os tensores em um arquivo .pt
torch.save({'X': X_tensor, 'y': y_tensor}, 'dados_treino.pt')
print("✅ Dados convertidos e salvos em 'dados_treino.pt'")