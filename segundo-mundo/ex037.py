# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numeroInteiro = int(input("Digite o número inteiro: "));
baseConversao = int(input("""Insira a base de conversão:
    1 - Binário
    2 - Octal
    3 - Hexadecimal
    Digite um dos valores citados: """));

if baseConversao > 0 and baseConversao < 4:
    if baseConversao == 1:
        print(f"O número {numeroInteiro} em binário é: {numeroInteiro:b}");
    elif baseConversao == 2:
        print(f"O número {numeroInteiro} em Octal é: {numeroInteiro:o}");
    else:
        print(f"O número {numeroInteiro} em hexadecimal é: {numeroInteiro:x}");

else:
    print("Valor inserido para a base de conversão incorreto");