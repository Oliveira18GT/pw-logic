nome = input("Seu nome: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = nota1 + nota2 + nota3 / 3

print(f"{nome}, sua média é: {media}")
    if media >= 16:
        print("Parabéns! Você foi aprovado.")
        else media < 16:
            print("Infelizmente, você não foi aprovado.")