# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

primeiroInteiro = int(input("Insira um número inteiro: "));
segundoInteiro = int(input("Insira um número inteiro: "));

if primeiroInteiro > segundoInteiro:
    print("O primeiro valor é maior.");

elif segundoInteiro > primeiroInteiro:
    print("O segundo valor é maior.");

else:
    print("Não existe valor maior, os dois são iguais.");