numeros = []  # lista vazia
i = 0
maiorNumero = 0

while i < 5:
    n = int(input("Informe o " + str(i + 1) + " numero: "))
    numeros.append(n)  # adiciona na lista

    if i == 0 or n > maiorNumero:
        maiorNumero = n

    i += 1  # sempre incrementa

print("\nMaior número:", maiorNumero)
