print("=== CONVERSOR DE ARMAZENAMENTO ===")

bytes = float(input("Digite a quantidade em bytes: "))
kb = float(input("Digite a quantidade de KB: "))
mb = float(input("Digite a quantidade de MB: "))

resultado_kb = bytes / 1024
resultado_mb = kb / 1024
resultado_gb = mb / 1024

print("=== RESULTADOS ===")

print(f"{bytes} bytes = {resultado_kb:.2f} KB")
print(f"{kb} KB = {resultado_mb:.2f} MB")
print(f"{mb} MB = {resultado_gb:.2f} GB")
print("=== FIM DO PROGRAMA ===")