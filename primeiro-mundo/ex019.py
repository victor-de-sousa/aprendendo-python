# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

primeiroAluno = str(input("Digite o nome de um aluno: "));
segundoAluno = str(input("Digite o nome de um aluno: "));
terceiroAluno = str(input("Digite o nome de um aluno: "));
quartoAluno = str(input("Digite o nome de um aluno: "));

alunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno];

alunoEscolhido = random.choice(alunos);



print(f"O aluno escolhido foi: {alunoEscolhido}");

