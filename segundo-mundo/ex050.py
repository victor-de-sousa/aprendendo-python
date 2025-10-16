# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

par = 0;

for quantidade in range(0, 6):
    numero = int(input("Digite um número inteiro: "));
    if numero % 2 == 0:
        par = par + numero;

print(par)