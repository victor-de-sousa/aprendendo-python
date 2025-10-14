# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint;

jogadaUsuario = int(input("""Vamos jogar!
    1 - Pedra
    2 - Papel
    3 - Tesoura"""));

computador = randint(1,3);

if jogadaUsuario > 0 and jogadaUsuario < 4:
    if jogadaUsuario == computador:
        print("PARABÉNSS, você ganhou!");
    else:
        print("QUE PENA, você perdeu!");
else:
    print("Valor inserido inválido.");