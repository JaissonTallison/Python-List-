# Calcule a média de três notas de um aluno e informe se ele foi aprovado (média maior ou igual a 7) ou reprovado.

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do Aluno foi: {media:.2f}")

if (media >= 7):
    print("APROVADO!")
else:
    print("REPROVADO!")
