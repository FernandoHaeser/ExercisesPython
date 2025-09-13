peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura(m): '))

imc = peso / (altura * altura)

print(f'\nSeu IMC é igual a: {imc: .2f}')

