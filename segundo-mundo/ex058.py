# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint;

computador = randint(0, 10);

respostaUsuario = int(input("De 0 a 10, tente acertar o número que o computador pensou: "));

while respostaUsuario != computador:
    respostaUsuario = int(input("Você errou! Tente novamente acertar o número que o computador pensou: "));

print(f"Você acertouu, o número era {respostaUsuario}");