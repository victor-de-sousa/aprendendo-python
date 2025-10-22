# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint;

computador = randint(0, 10);

respostaUsuario = 11;
palpites = 0;


while respostaUsuario != computador:
    respostaUsuario = int(input("Tente acertar o número que o computador pensou! Insira aqui: "));
    palpites+=1;
    while respostaUsuario != computador:
        if respostaUsuario < computador:
            respostaUsuario = int(input(f"Errou, o número é maior que {respostaUsuario}!, tente novamente: "));
        else:
            respostaUsuario = int(input(f"Errou, o número é menor que {respostaUsuario}!, tente novamente: "));
        palpites+=1;
            
print(f"Você acertou o número com {palpites} palpites!");