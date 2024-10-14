# Faça um programa que receba o valor de um salário e o percentual de aumento. Calcule e exiba o novo salário com o reajuste aplicado.

def calcular_novo_salario(salario, percentual_aumento):

    percentual_decimal = percentual_aumento / 100

    aumento = salario * percentual_decimal

    novo_salario = salario + aumento

    return novo_salario


salario_atual = float(input("Digite o valor do salário atual: "))
aumento = float(input("Digite o percentual de aumento: "))

novo_salario = calcular_novo_salario(salario_atual, aumento)
print(f"O novo salário é: R$ {novo_salario:.2f}")
