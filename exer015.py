# Faça um programa que leia um valor de hora e o valor que você ganha por hora. Em seguida, calcule e exiba o salário mensal considerando 160 horas trabalhadas no mês.

def calcular_salario():

    valor_por_hora = float(input("Digite o valor ganho por hora: "))
    horas_trabalhadas = 160

    sal_mensal = valor_por_hora * horas_trabalhadas

    print(f"Seu salário mensal é de R$ {sal_mensal:.2f}")


calcular_salario()
