# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime;

anoNascimento = int(input("Digite o seu ano de nascimento: "));

anoAtual = datetime.now().year

idade = anoAtual - anoNascimento;

if idade < 18:
    print("Ainda vai se alistar ao serviço militar.");

elif idade == 18:
    print("Agora é a hora de se alistar.");

else:
    print("Já passou do tempo do alistamento");