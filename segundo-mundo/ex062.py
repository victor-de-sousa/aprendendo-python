# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input("Digite o primeiro termo da PA: "));
razao = int(input("Digite a razão da PA: "));

termo = 0;
quantidadePosicoes = 0;
termoUser = 10

while termoUser > 0:

    while quantidadePosicoes < termoUser:
        quantidadePosicoes += 1;
        termo = primeiroTermo + (quantidadePosicoes - 1) * razao;
        print(termo);
    
    termoUser = int(input("Você deseja mostrar mais quantos termos? "));

    if termoUser != 0:
        termoUser += quantidadePosicoes; 