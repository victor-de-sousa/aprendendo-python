# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while


primeiroTermo = int(input("Digite o primeiro termo da PA: "));
razao = int(input("Digite a razão da PA: "));
termo = 0;

quantidadePosicoes = 0;

while quantidadePosicoes != 10:
    quantidadePosicoes+=1;
    termo = primeiroTermo + (quantidadePosicoes - 1) * razao;
    print(termo);

