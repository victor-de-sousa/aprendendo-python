# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

pares = 0

print("Os números pares entre 1 a 50 são:")

for pares in range(1, 50):
    pares+=1;
    if pares % 2 == 0:
        print(pares);