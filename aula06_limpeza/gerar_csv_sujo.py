import pandas as pd
import numpy as np

# Criando dados com problemas propositais (NaN = Not a Number / Vazio)
dados = {
    "id_cliente": [101, 102, 103, 104, 105, 106],
    "nome": ["Ana", "Bruno", "Carlos", np.nan, "Eduarda", "Felipe"],
    "renda_mensal": ["5000", "3200", np.nan, "4100", "ERROR", "6000"],
    "idade": [25, 30, 22, 45, np.nan, 35],
    "score_credito": [850, np.nan, 400, 750, 600, 900]
}

df = pd.DataFrame(dados)

# Salvando como CSV para usarmos
df.to_csv("dados_brutos.csv", index=False)

print("✅ Arquivo 'dados_brutos.csv' gerado com sucesso!")