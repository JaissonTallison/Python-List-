# Desenvolva um programa que leia um número inteiro e exiba seu dobro, triplo e raiz quadrada. Utilize os operadores aritméticos.

import math

num = int(input("Digite o Número: "))


dobro = (num * 2)

triplo = (num * 3)

raiz_qua = math.sqrt(num)

print(f"O número {num}, Dobro {dobro}, Triplo {
      triplo} e Raiz quadrada {raiz_qua:.2f}")
