# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

multiplo = 0;

for multiplo in range(1, 20):
    multiplo += 1;
    if multiplo % 3 == 0:
        print(multiplo);