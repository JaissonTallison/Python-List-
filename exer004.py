# Armazene o preço de um produto e o percentual de desconto em duas variáveis. Calcule e exiba o valor final do produto após o desconto sabendo que a fórmula para obter este valor é: Valor do Protudo x (1 - (Desconto / 100)).

preco = float(input("Digite o preço: "))
desc = float(input("Digite o percentual de desconto: "))

precoDesconto = preco * (desc / 100)

precoFinal = preco - precoDesconto

print(f"O preço final do produto com desconto é: {precoFinal}")
