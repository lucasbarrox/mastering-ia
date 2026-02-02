import torch
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt


# Baixar o dataset FashionMNIST
train_data = datasets.FashionMNIST(
    root="data",         # Onde salvar
    train=True,          # Quero os dados de treino
    download=True,       # Baixar da internet
    transform=ToTensor() # Converter imagem (jpg) para Tensor (matriz de numeros)
)

print(f"Total de Imagens: {len(train_data)}")
print(f"Tamanho da Imagem: {train_data[0][0].shape}") 
# [1, 28, 28] -> 1 Canal (Preto e branco), 28px altura, 28px largura

# Mapear os rótulos para nomes legíveis
class_names = {
    0: "Camiseta/Top", 1: "Calça", 2: "Pullover", 3: "Vestido", 4: "Casaco",
    5: "Sandália", 6: "Camisa", 7: "Tênis", 8: "Bolsa", 9: "Bota"
}

# Visualizar algumas imagens do dataset
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3

for i in range(1, cols * rows + 1):
    # Pega um índice aleatório
    sample_idx = torch.randint(len(train_data), size=(1,)).item()
    img, label = train_data[sample_idx]
    
    figure.add_subplot(rows, cols, i)
    plt.title(class_names[label])
    plt.axis("off")
    # squeeze() remove a dimensão de cor 1 para plotar em escala de cinza
    plt.imshow(img.squeeze(), cmap="gray")

plt.savefig("amostra_roupas.png")
print("✅ Imagem 'amostra_roupas.png' salva. Confira os dados!")