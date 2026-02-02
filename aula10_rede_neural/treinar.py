import torch
from torch import nn
from rede_neural import ClassificadorCirculos # Importando nossa classe

print("--- 🏋️ Iniciando Treinamento Neural ---")

# Carregar Dados
dados = torch.load('dados_treino.pt')
X = dados['X']
y = dados['y'].unsqueeze(1) # Ajustar shape para (N, 1)

# Dividir em Treino e Teste (80% Treino, 20% Teste)
split = int(0.8 * len(X))
X_train, y_train = X[:split], y[:split]
X_test, y_test = X[split:], y[split:]

# CONFIGURAR MODELO, FUNÇÃO DE ERRO E OTIMIZADOR
modelo = ClassificadorCirculos()
loss_fn = nn.BCELoss() # Binary Cross Entropy Loss

# O Otimizador vai mexer nos parametros do modelo. Learning Rate (lr) é a velocidade.
optimizer = torch.optim.SGD(params=modelo.parameters(), lr=0.1)

# TREINAMENTO
epochs = 1000

for epoch in range(epochs):
    modelo.train() # Modo de treino (ativa aleatoriedades se houver)
    
    # --- Passada de Treinamento ---
    # A) Forward Pass (Chutar uma saída com os dados de treino)
    y_pred = modelo(X_train)
    
    # B) Calcular o Erro (Loss)
    loss = loss_fn(y_pred, y_train)
    
    # C) Zerar os gradientes antes do backward pass
    optimizer.zero_grad()
    
    # D) Backward Pass (Calcular os gradientes)
    loss.backward()
    
    # E) Atualizar os pesos
    optimizer.step()
    
    # --- Avaliação a cada 100 épocas ---
    if epoch % 10 == 0:
        modelo.eval() # Modo de avaliação (desativa aleatoriedades se houver)
        with torch.inference_mode():
            test_pred = modelo(X_test)
            test_loss = loss_fn(test_pred, y_test)
            # Acurácia: Quantos % ela acertou? (Arredonda > 0.5 vira 1, < 0.5 vira 0)
            acertos = ((test_pred > 0.5) == y_test).sum().item()
            acc = acertos / len(y_test)
            
        print(f"Época {epoch} | Erro Treino: {loss:.4f} | Erro Teste: {test_loss:.4f} | Acurácia: {acc:.2%}")

print("\n✅ Treinamento Finalizado!")
print("Se a Acurácia final for > 99%, sua rede aprendeu a desenhar um círculo!")

# Salvar o modelo treinado
torch.save(modelo.state_dict(), "modelo_circulos.pth")