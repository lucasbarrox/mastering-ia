# fazendo a importação da 'biblioteca' que criamos
import analise

# dados simulados
minha_carteira = [
    {"nome": "Bitcoin",  "ticker": "BTC", "qtd": 0.1, "preco_unitario": 98000.00},
    {"nome": "Ethereum", "ticker": "ETH", "qtd": 2.0, "preco_unitario": 2800.00},
    {"nome": "Solana",   "ticker": "SOL", "qtd": 5.0, "preco_unitario": 110.00},
    {"nome": "Cardano",  "ticker": "ADA", "qtd": 1000.0, "preco_unitario": 0.60} 
]

print("--- 🏦 Sistema de Análise Financeira Modular ---")

# Chamando a função da NOSSA biblioteca
total_patrimonio, lista_baleias = analise.calcular_resumo(minha_carteira)

# Chamando a outra função
top_coin = analise.obter_ativo_top(minha_carteira)

patrimonio_usd = analise.converter_para_dolar(total_patrimonio, 5)

# Exibindo resultados
print(f"Patrimônio Total: R$ {total_patrimonio:,.2f}")
print(f"Ativos 'Baleia':  {lista_baleias}")
print(f"Principal Ativo:  {top_coin}")
print(f"Patrimônio Total em $: {patrimonio_usd:,.2f}")