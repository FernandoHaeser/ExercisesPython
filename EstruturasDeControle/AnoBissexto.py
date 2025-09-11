ano = int(input("Informe um ano: "))

if (ano % 4 == 0) or (ano % 100 == 0) or (ano % 400 == 0):
    print("\nSeu ano é bissexto")
else:
    print("\nSeu ano nao e bissexto")