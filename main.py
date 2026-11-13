print("=== CALCULADORA DE DESCONTO ===")
produto = input("Nome do produto: ")
preco = float(input("Preço R$: "))
desconto = float(input("Desconto (%): ")).replace(("," "."))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"\nProduto: {produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: R$ {desconto:.2f}%")
print(f"Preço final: R$ {preco_final:.2f}")
