#Crie um dicionário com informações de uma pessoa (nome, idade, cidade) e mostre cada chave e valor.

pessoa = {
    "nome": "Fernando Augusto Haeser",
    "idade": 19,
    "sexo": "Masculino",
    "salario": 2750,
    "cidade": "Viamão"
}

for chaves, valor in pessoa.items():
    print("Chave:",chaves)
    print("Valor:",valor)
    print("--------------")