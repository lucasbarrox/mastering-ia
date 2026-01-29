import pandas as pd
import matplotlib.pyplot as plt

print("--- 📊 Gerador de Gráficos v1.0 ---")

# DADOS
dados = {
    "Mes": ["Jan", "Fev", "Mar", "Abr", "Mai"],
    "Preco_BTC": [42000, 45000, 68000, 62000, 71000],
    "Preco_ETH": [2200, 2400, 3500, 3100, 3800]
}

# CRIANDO O DATAFRAME
# DataFrame é o nome chique para "Tabela de Excel no Python"
df = pd.DataFrame(dados)

print("\nVisualizando a Tabela de Dados:")
print(df) # Mostra a tabelano terminal

#GERANDO O GRÁFICO
print("\nGerando gráfico...")

# Tamanho da figura (10 polegadas de largura, 5 de altura)
plt.figure(figsize=(10, 5))

# Desenhando as linhas
# Eixo X = Coluna 'Mes', Eixo Y = Coluna 'Preco_BTC'
plt.plot(df['Mes'], df['Preco_BTC'], label='Bitcoin (BTC)', color='orange', marker='o')
plt.plot(df['Mes'], df['Preco_ETH'], label='Ethereum (ETH)', color='blue', marker='s')

# Decorando o gráfico
plt.title('Evolução do Preço: BTC vs ETH (2026)')
plt.xlabel('Mês')
plt.ylabel('Preço em USD')
plt.legend() # Mostra a legenda das linhas
plt.grid(True) # Coloca as linhas de grade no fundo

# SALVANDO O ARQUIVO
nome_arquivo = "evolucao_crypto.png"
plt.savefig(nome_arquivo)

print(f"✅ Gráfico salvo com sucesso: {nome_arquivo}")
print("Olhe na barra lateral esquerda (Explorer) para ver a imagem!")