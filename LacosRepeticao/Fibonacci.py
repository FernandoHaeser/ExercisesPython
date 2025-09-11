n1 = 0
n2 = 1
cont = 0

while cont < 10:
    print(n1)
    proximo = n1 + n2
    n1 = n2
    n2 = proximo
    cont += 1
