import math

a = float(input('Informe o valor A da equacao: '))
b = float(input('Informe o valor B da equacao: '))
c = float(input('Informe o valor C da equacao: '))

delta = (b*b) - 4 * a * c

if (delta < 0):
    print('\nDelta é negativo, a equação não possui raizes reais.')
    exit()

deltaR = math.sqrt(delta)

resultPlus = (b * (-1)) + deltaR / (2 * a)
resultMinus = (b * (-1)) - deltaR / (2 * a)

print(f'\nO valor de delta é: {deltaR:.2f}')
print(f'O valor de X1 é: {resultPlus:.2f}')
print(f'O valor de X2 é: {resultMinus:.2f}')