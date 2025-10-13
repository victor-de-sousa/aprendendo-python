# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um número inteiro: "));

identificadorNumero = numero % 2;

if identificadorNumero == 0:
    print(f"O número {numero} é PAR");
else:
    print(f"O número {numero} é ÍMPAR");
