# Escreva um programa que leia o valor de um depósito bancário e um valor de juros anual. Calcule e exiba o valor acumulado após 1, 5 e 10 anos, considerando juros compostos.

def calcular_juros_compostos(valor_inicial, taxa_juros, tempo):

    valor_final = valor_inicial * (1 + taxa_juros/100) ** tempo
    return valor_final


valor_deposito = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual (%): "))

valor_1_ano = calcular_juros_compostos(valor_deposito, taxa_juros, 1)
valor_5_anos = calcular_juros_compostos(valor_deposito, taxa_juros, 5)
valor_10_anos = calcular_juros_compostos(valor_deposito, taxa_juros, 10)

print(f"Valor acumulado após 1 ano: R$ {valor_1_ano:.2f}")
print(f"Valor acumulado após 5 anos: R$ {valor_5_anos:.2f}")
print(f"Valor acumulado após 10 anos: R$ {valor_10_anos:.2f}")
