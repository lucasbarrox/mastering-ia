import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
from modelo_cnn import RedeNeuralVisao # Importa a arquitetura da rede neural

print("--- 🏗️ Preparando Treino ---")

# Dados e Loaders
train_data = datasets.FashionMNIST(root="data", train=True, download=True, transform=ToTensor())
test_data = datasets.FashionMNIST(root="data", train=False, download=True, transform=ToTensor())

# DataLoaders (Carregadores de Dados)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

# Modelo, Função de Perda e Otimizador
modelo = RedeNeuralVisao()
loss_fn = nn.CrossEntropyLoss() # Padrão para multiclasse (10 roupas)
optimizer = torch.optim.Adam(modelo.parameters(), lr=0.001) # Adam é melhor/mais rápido que SGD

# Função de Treino
def train_step(dataloader, model, loss_fn, optimizer):
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        # Forward
        pred = model(X)
        loss = loss_fn(pred, y)
        
        # Backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 400 == 0:
            print(f"   Lote {batch}/{len(dataloader)} | Erro: {loss.item():.4f}")

# Função de Teste
def test_step(dataloader, model, loss_fn):
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            # A classe vencedora é a que tem o maior valor (argmax)
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
            
    correct /= len(dataloader.dataset)
    print(f"   📝 Acurácia de Teste: {100*correct:.1f}%")

# Loop de Treino
print("\n--- 🚀 Iniciando Treino ---")
epochs = 3 # Número de vezes que o modelo verá todo o dataset
for t in range(epochs):
    print(f"\n--- Época {t+1} ---")
    train_step(train_loader, modelo, loss_fn, optimizer)
    test_step(test_loader, modelo, loss_fn)

print("\n✅ Treino Concluído!")
torch.save(modelo.state_dict(), "modelo_roupas.pth")