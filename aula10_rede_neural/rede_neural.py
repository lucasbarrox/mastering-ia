import torch
from torch import nn

# Definindo a arquitetura da Rede Neural
class ClassificadorCirculos(nn.Module):
    def __init__(self):
        super().__init__()
        
        # CAMADA 1: Recebe 2 features (x1, x2), cospe 10 novas features
        self.camada_1 = nn.Linear(in_features=2, out_features=10)
        
        # CAMADA 2: Recebe 10, cospe 10
        self.camada_2 = nn.Linear(in_features=10, out_features=10)
        
        # CAMADA DE SAÍDA: Recebe 10, cospe 1 (Probabilidade da classe ser 1)
        self.camada_saida = nn.Linear(in_features=10, out_features=1)
        
        # ATIVAÇÃO: ReLU
        # Transforma números negativos em 0, mantém positivos
        self.relu = nn.ReLU()
        
        # ATIVAÇÃO: Sigmoid
        # Transforma a saída em valor entre 0 e 1 (Probabilidade)
        self.sigmoid = nn.Sigmoid()

    # Definindo o fluxo de dados pela rede
    def forward(self, x):
        # Entra -> Camada 1 -> ReLU (dobra) -> Camada 2 -> ReLU (dobra) -> Saída -> Sigmoid
        z = self.camada_1(x)
        z = self.relu(z) 
        z = self.camada_2(z)
        z = self.relu(z)
        z = self.camada_saida(z)
        output = self.sigmoid(z)
        return output

# Teste rápido para ver se a arquitetura está correta
if __name__ == "__main__":
    modelo = ClassificadorCirculos()
    print(modelo)
    print("✅ Arquitetura definida com sucesso!")