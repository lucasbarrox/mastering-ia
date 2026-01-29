import numpy as np

print("--- 🧠 Simulador de Neurônio Artificial (NumPy) ---")

# DADOS DE ENTRADA (Inputs - X)
# Imagine um cliente pedindo empréstimo:
# [Renda Mensal (milhares), Idade, Histórico de Crédito (0-10)]
inputs = np.array([1.5, 20.0, 2.0]) 

# PESOS (Weights - W)
# O que a IA aprendeu que é importante:
# [Alta importância pra Renda, Baixa pra Idade, Alta pro Histórico]
weights = np.array([0.8, 0.1, 0.5])

# VIÉS (Bias - b)
# Um valor base para ajustar a ativação (como um "chute inicial")
bias = -2.0

print(f"Inputs (X):  {inputs}")
print(f"Pesos (W):   {weights}")
print(f"Bias (b):    {bias}")

# A MATEMÁTICA (Produto Escalar / Dot Product)
# Fórmula: (input1 * peso1) + (input2 * peso2) + ... + bias
output = np.dot(inputs, weights) + bias

print("\n--- Processamento ---")
print(f"Cálculo: ({inputs[0]}*{weights[0]}) + ({inputs[1]}*{weights[1]}) + ({inputs[2]}*{weights[2]}) + ({bias})")
print(f"Resultado (Score): {output:.2f}")

# FUNÇÃO DE ATIVAÇÃO (A Decisão)
# Se o score for positivo, aprova. Se negativo, reprova. (Função Step simples)
if output > 0:
    print("\n✅ Decisão da IA: EMPRÉSTIMO APROVADO")
else:
    print("\n❌ Decisão da IA: EMPRÉSTIMO NEGADO")