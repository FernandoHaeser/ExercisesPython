num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print("\n", num1, "é o maior número!")
elif num2 > num1 and num2 > num3:
    print("\n", num2, "é o maior número!")
else:
    print("\n", num3, "é o maior número!")
