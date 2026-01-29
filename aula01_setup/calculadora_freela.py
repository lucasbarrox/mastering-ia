import math #importando biblioteca nativa de matematica 

print("--- 💰 Calculadora de Viabilidade de Freelance ---")

# ENTRADA DE DADOS
# O float() converte o texto digitado para número decimal imediatamente
projeto = input("Nome do Projeto: ")
valor_total = float(input("Valor total do projeto (R$): "))
horas_estimadas = int(input("Horas estimadas para concluir: "))
sua_hora_base = float(input("Qual sua meta de valor/hora (ex: 90.00)? "))

# Lógica

# Calculamos quanto esse projeto está pagando por hora na realidade
valor_hora_real = valor_total / horas_estimadas

# Calculamos a diferença
diferenca = valor_hora_real - sua_hora_base

# Regra de Decisão
vale_a_pena = valor_hora_real >= sua_hora_base

# SAÍDA DE DADOS
print("\n" + "="*40)
print(f"Relatório para: {projeto}")
print("="*40)
print(f"Valor Hora Real: R$ {valor_hora_real:.2f}")
print(f"Sua Meta:        R$ {sua_hora_base:.2f}")

if vale_a_pena:
    print(f"✅ APROVADO! Você está ganhando R$ {diferenca:.2f} acima da sua meta.")
    print("Dica: Tente fechar hoje.")
else:
    # A função abs() pega o valor absoluto
    print(f"❌ CUIDADO! Você está perdendo R$ {abs(diferenca):.2f} por hora.")
    print("Dica: Negocie um valor maior ou diminua o escopo.")