# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep;

contagemRegressiva = 11

print("\033[31m------Contagem Regressiva------\033[m")

for contagem in range(1, 11):
    contagemRegressiva-=1
    print(contagemRegressiva)
    sleep(1);

print("!!!ESTOURO DOS FOGOS DE ARTIFÍCIOOOO!!!!")