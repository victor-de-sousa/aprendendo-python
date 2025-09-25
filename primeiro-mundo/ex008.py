# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input("Digite um valor em metros: "));

centimetros = valor/100;
militimetros = valor/1000;

print(f"{valor:.2f} metros\nEm centímetros é igual a: {centimetros:.2f}\nEm milímetros é igual a {militimetros:2f}");