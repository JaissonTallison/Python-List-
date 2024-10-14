# Crie um programa que converta a idade do usuário de anos para meses. Suponha que 1 ano tenha 12 meses. A idade deve ser informada através do teclado.

nome = input("Informe seu nome: ")
idade = int(input("Informe sua Idade: "))

mes = idade * 12

print(f"Olá, {nome}! Sua Idade em meses é: {mes}")
