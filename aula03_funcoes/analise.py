# Recebe uma lista de ativos e retorna o patrimônio total e a lista de ativos 'Baleia' (> 1000 reais)
def calcular_resumo(carteira):
    total = 0
    baleias = []

    # mesma logica da aula 02
    for ativo in carteira:
        valor = ativo["qtd"] * ativo["preco_unitario"]
        total += valor

        if valor > 1000:
            baleias.append(ativo["ticker"])

    # retorna os dados pra quem chamou a função
    return total, baleias

# retorna o nome do ativo com maior valor na carteira
def obter_ativo_top(carteira):
    maior_valor = 0
    nome_top = ""

    for ativo in carteira:
        valor = ativo["qtd"] * ativo["preco_unitario"]
        if valor > maior_valor:
            maior_valor = valor
            nome_top = ativo["nome"]
            
    return nome_top

def converter_para_dolar(valor_reais, taxa_dolar):
    return valor_reais / taxa_dolar