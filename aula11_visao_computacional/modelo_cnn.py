from torch import nn

class RedeNeuralVisao(nn.Module):
    def __init__(self):
        super().__init__()
        
        # BLOCO CONVOLUCIONAL 1
        # Entra imagem 28x28 (1 canal - preto e branco)
        self.layer1 = nn.Sequential(
            # Conv2d(in_channels, out_channels, kernel_size)
            # Cria 16 mini-filtros de tamanho 3x3 que varrem a imagem
            nn.Conv2d(1, 16, kernel_size=3, padding=1), 
            nn.ReLU(),
            # MaxPool2d(2) -> Reduz a imagem pela metade (pega o maior valor de cada quadrado 2x2)
            # Imagem cai de 28x28 -> 14x14
            nn.MaxPool2d(kernel_size=2)
        )
        
        # BLOCO CONVOLUCIONAL 2
        # Entra 14x14 (16 canais vindos de cima)
        self.layer2 = nn.Sequential(
            # Cria 32 filtros baseados nos 16 anteriores
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            # Reduz pela metade de novo: 14x14 -> 7x7
            nn.MaxPool2d(2)
        )
        
        # CLASSIFICADOR FINAL (Dense Layer)
        self.flatten = nn.Flatten() # Achata a saída para um vetor
        
        # Cálculo: 32 canais * 7 largura * 7 altura = 1568 neurônios de entrada
        self.classifier = nn.Linear(32 * 7 * 7, 10) # 10 classes de saída

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.flatten(x)
        logits = self.classifier(x)
        return logits