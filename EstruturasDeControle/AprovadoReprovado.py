nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

aprovadoReprovado = ("\nAprovado!, sua média foi", media) if media >= 7 else ("\nReprovado!, sua média foi", media)

print(aprovadoReprovado)