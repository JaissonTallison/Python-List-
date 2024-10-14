# Escreva um programa que leia um número e exiba a tabuada desse número de 1 a 10.

def tabuada(numero):

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


numero = int(input("Digite um número para ver sua tabuada: "))

tabuada(numero)
