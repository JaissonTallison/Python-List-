# Crie um programa que leia o nome, a idade e o salário de uma pessoa. Exiba essas informações formatadas como uma ficha pessoal.

def criar_ficha_pessoal():

    nome = input("Digite seu nome completo: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))

    ficha = f"""


    Nome: {nome}
    Idade: {idade} anos
    Salário: R$ {salario:.2f}
    """

    return ficha


ficha_completa = criar_ficha_pessoal()
print(ficha_completa)
