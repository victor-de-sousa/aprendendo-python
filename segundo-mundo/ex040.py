# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

primeiraNota = int(input("Digite a nota do aluno: "));
segundaNota = int(input("Digite a nota do aluno: "));

media = (primeiraNota + segundaNota) / 2;

if media >= 5:
    if media < 7:
        print("RECUPERAÇÃO!");
    else:
        print("APROVADO");

else:
    print("REPROVADO!");