import torch

print("--- ✨ PyTorch Autograd (Cálculo Automático) ---")

# Definindo a variável X
# requires_grad=True diz ao PyTorch para rastrear todas as operações com esse tensor
x = torch.tensor(2.0, requires_grad=True)

# Definindo a Equação: y = x² + 3x + 5
# Como x vale 2: y = 4 + 6 + 5 = 15
y = x**2 + 3*x + 5

print(f"Valor de x: {x.item()}")
print(f"Resultado da equação (y): {y.item()}")

# Calculando o Gradiente
# Chama o backward() na saída para calcular o gradiente
y.backward()

# Mostrando o Gradiente
# O gradiente de y em relação a x é armazenado em x.grad
print("\n--- Resultado do Cálculo Diferencial ---")
print(f"A derivada de (x² + 3x + 5) quando x=2 é: {x.grad.item()}")

print("\n--- Conferência Manual ---")
print("Derivada teórica: 2x + 3")
print(f"Cálculo: 2(2) + 3 = {2*2 + 3}")

if x.grad.item() == 7.0:
    print("\n✅ O PyTorch acertou a derivada exata!")
else:
    print("\n❌ Algo deu errado.")