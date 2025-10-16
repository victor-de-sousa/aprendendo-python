# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime;

ano = datetime.datetime.now().year;

quantidadeAtingiram = 0;
quantidadeNãoAtingiram = 0;

for pessoa in range(0, 7):
    anoNascimento = int(input("Digite o seu ano de nascimento: "));
    if ano - anoNascimento < 18:
        quantidadeNãoAtingiram += 1;
    else:
        quantidadeAtingiram += 1;

print(f"""Quantidade de pessoas que
    Não atingiram a maioridade: {quantidadeNãoAtingiram}
    Atingiram a maioridade: {quantidadeAtingiram}""");