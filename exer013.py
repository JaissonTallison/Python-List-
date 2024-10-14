# Escreva um programa que leia dois números inteiros e exiba o quociente e o resto da divisão entre eles usando os operadores // (divisão inteira) e % (módulo).

def divisao_e_resto(numerador, denominador):

    if denominador == 0:
        return "Divisão por zero não é permitida."

    quociente = numerador // denominador
    resto = numerador % denominador
    return quociente, resto


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número (divisor): "))

resultado = divisao_e_resto(num1, num2)

if isinstance(resultado, tuple):
    quociente, resto = resultado
    print(f"O quociente da divisão é: {quociente}")
    print(f"O resto da divisão é: {resto}")
else:
    print(resultado)
