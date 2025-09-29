# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

primeiroAluno = str(input("Digite o nome do aluno: "));
segundoAluno = str(input("Digite o nome do aluno: "));
terceiroAluno = str(input("Digite o nome do aluno: "));
quartoAluno = str(input("Digite o nome do aluno: "));

alunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno];

random.shuffle(alunos);

print(alunos);