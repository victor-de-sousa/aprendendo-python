# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numeroInteiro = int(input("Digite um número inteiro: "));

for divisores in range(2, numeroInteiro):
    if numeroInteiro % divisores == 0:
        print("Não é um número primo.");
        break
    else:
        print("É um número primo.")  