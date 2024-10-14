# Crie um programa que calcule a média ponderada de um aluno. O programa deve ler três notas e seus respectivos pesos, calcular e exibir a média ponderada.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

peso1 = 1
peso2 = 2
peso3 = 3

media_ponderada = ((nota1 * peso1) + (nota2 * peso2) +
                   (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A média ponderada do aluno é: {media_ponderada}")
