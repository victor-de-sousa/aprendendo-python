# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex:

# 5! = 5x4x3x2x1 = 120

numeroUser = int(input("Digite um número: "));

numeroConta = numeroUser;

fatorial = 1;

while numeroConta != 0:
    fatorial = numeroConta * fatorial;
    numeroConta-=1;

print("O fatorial do número {} é igual à {}.".format(numeroUser, fatorial));