# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite aqui o seu salario: "));

aumento = salario * 1.15;

print(f"O seu salário que era de R$ {salario:.2f} agora após o aumento está R$ {aumento:.2f}");