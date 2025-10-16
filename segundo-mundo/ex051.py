# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("PROGRESSÃO ARITMÉTICA");

primeiroTermo = int(input("Digite o primeiro termo da PA: "));
razao = int(input("Digite a razão da PA: "));
posicao = 0;
termo = 0;

print("\n=-=-=-PRIMEIROS TERMOS-=-=-=\n")

for termos in range(0, 10):
    posicao += 1;
    termo = primeiroTermo + (posicao - 1) * razao;
    print(termo)

