import pandas as pd

dados = {
    "cliente": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
    "idade": [23, 35, 29, 40, 31],
    "valor_compra": [100, 250, 80, 300, 150]
}

df = pd.DataFrame(dados)

# Segmento jovem
segmento_jovem = df[df["idade"] < 30]

# Alto valor
cliente_potencial_alto = df[(df["valor_compra"] > 100) & (df["idade"] > 30)]

# Baixo valor
cliente_potencial_baixo = df[(df["valor_compra"] < 200) | (df["idade"] < 25)]

print("Segmento jovem:")
print(segmento_jovem)

print("\nClientes de alto valor:")
print(cliente_potencial_alto)

print("\nClientes de baixo potencial:")
print(cliente_potencial_baixo)