# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint;

print("----ACERTE O NÚMERO INTEIRO----")

respostaUsuario = int(input("Digite algum número para a tentativa: "));

computador = randint(1, 5);


if respostaUsuario == computador:
    print("PARABÉNS, você acertou!!");
else:
    print("Você errou :(");

print(f"A resposta era: {computador}");