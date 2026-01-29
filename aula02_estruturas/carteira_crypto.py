print("--- 🚀 Crypto Wallet Manager v1.0 ---")

# DADOS (Simulando o que viria de uma API)
# LISTA de DICIONÁRIOS.
carteira = [
    {"nome": "Bitcoin",  "ticker": "BTC", "qtd": 0.05, "preco_unitario": 98000.00},
    {"nome": "Ethereum", "ticker": "ETH", "qtd": 1.20, "preco_unitario": 2800.00},
    {"nome": "Solana",   "ticker": "SOL", "qtd": 15.0, "preco_unitario": 110.50},
    {"nome": "Dogecoin", "ticker": "DOGE", "qtd": 5000, "preco_unitario": 0.15},
    {"nome": "Cardano",  "ticker": "ADA", "qtd": 1000, "preco_unitario": 0.60},
]

# PROCESSAMENTO
patrimonio_total = 0
ativos_relevantes = [] # Lista para guardar só o que vale a pena

print("\nProcessando seus ativos...\n")

# Loop FOR: Para cada 'ativo' dentro da 'carteira'
for ativo in carteira:
    # Calculando o valor total do ativo
    valor_posicao = ativo["qtd"] * ativo["preco_unitario"]
    
    # Acumulando no total geral
    patrimonio_total += valor_posicao
    
    # Lógica de decisão: Filtrar ativos
    if valor_posicao > 1000:
        ativos_relevantes.append(ativo["ticker"]) # Adiciona na lista de destaques
        status = "💎 (Baleia)"
    else:
        status = "🐟 (Sardinha)"

    # Exibindo linha a linha
    print(f"{status} {ativo['nome']}: R$ {valor_posicao:,.2f}")

# RELATÓRIO FINAL
print("\n" + "="*30)
print(f"💰 PATRIMÔNIO TOTAL: R$ {patrimonio_total:,.2f}")
print("="*30)

# Exibindo a lista de ativos relevantes
print(f"Ativos principais (> R$ 1k): {ativos_relevantes}")

# Distribuição (Simples estatística)
porcentagem_btc = (carteira[0]["qtd"] * carteira[0]["preco_unitario"]) / patrimonio_total
print(f"Dominância do Bitcoin: {porcentagem_btc:.1%} do portfólio")