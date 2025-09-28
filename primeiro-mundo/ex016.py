# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc;

numeroReal = float(input("Digite um número real: "));

porcaoInteira = trunc(numeroReal);

print(f"A porção inteira de {numeroReal} é {porcaoInteira}");
