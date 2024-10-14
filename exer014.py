# Crie um programa que converta uma medida de metros para centímetros e milímetros.

medida = float(input("Informe a medida: "))

centimetros = (medida * 100)

milimetros = (medida * 1000)

print(f"A medida {medida:.2f} metros equivale {
      centimetros:.2f} cm e {milimetros:.2f} mm")
