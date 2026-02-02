import torch
import numpy as np

print("--- 🥊 Round 1: Estrutura de Dados ---")

# Lista Python
lista = [1, 2, 3]

# NumPy Array
array_np = np.array(lista)

# PyTorch Tensor
tensor_pt = torch.tensor(lista)

print(f"NumPy:  {array_np} | Tipo: {type(array_np)}")
print(f"Tensor: {tensor_pt} | Tipo: {type(tensor_pt)}")

print("\n--- 🥊 Round 2: Matemática ---")
# Multiplicação por 2
print(f"NumPy * 2:  {array_np * 2}")
print(f"Tensor * 2: {tensor_pt * 2}")

print("\n--- 🥊 Round 3: A Diferença Crucial (Interoperabilidade) ---")
# Pode transformar um no outro sem perder dados
de_numpy_para_tensor = torch.from_numpy(array_np)
de_tensor_para_numpy = tensor_pt.numpy()

print("Conversão funcionou perfeitamente.")