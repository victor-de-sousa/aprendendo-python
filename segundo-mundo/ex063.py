# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

# Ex:

# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8



numero = int(input("Digite um número qualquer: "));

primeiroNumero = 0;
segundoNumero = 1;

fibonacci = 1;

contador = 0;

print(fibonacci);

while contador != numero:
    contador+=1;
    fibonacci = primeiroNumero + segundoNumero;
    print(fibonacci);
    primeiroNumero = segundoNumero;
    segundoNumero = fibonacci;

print("--FIM DA SEQUÊNCIA--");