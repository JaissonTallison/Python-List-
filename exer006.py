# Crie um programa que solicite ao usuário seu nome e idade e armazene esses valores. Exiba uma mensagem informando se o usuário é maior ou menor de idade.

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

print(f"Olá, {nome}! Vc tem {idade} anos.")

if (idade >= 18):
    print(f"vc é maior de Idade!!!")
else:
    print(f"vc é menor de Idade!!!")
