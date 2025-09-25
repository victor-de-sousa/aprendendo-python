# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Digite um número inteiro: "));

antecessor = numero - 1;
sucessor = numero + 1;

print(f'O número {numero} tem como:\n Antecessor: {antecessor};\n E como sucessor: {sucessor}.');
