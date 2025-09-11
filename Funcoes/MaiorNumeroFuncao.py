def maiornumero(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))

print("\nMaior valor:", maiornumero(n1, n2))