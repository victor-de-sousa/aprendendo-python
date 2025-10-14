# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

primeiraReta = int(input("Digite o comprimento de uma reta: "));
segundaReta = int(input("Digite o comprimento de uma reta: "));
terceiraReta = int(input("Digite o comprimento de uma reta: "));

if primeiraReta < (segundaReta + terceiraReta) and segundaReta < (primeiraReta + terceiraReta) and terceiraReta < (primeiraReta + segundaReta):
    if primeiraReta == segundaReta == terceiraReta:
        print("Triângulo Equilátero");
    elif primeiraReta == segundaReta or segundaReta == primeiraReta or terceiraReta == primeiraReta:
        print("Triângulo Isósceles");
    else:
        print("Triângulo Escaleno");

else:
    print("Você digitou comprimentos que não formam um triângulo.");