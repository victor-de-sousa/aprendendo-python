# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

primeiraReta = float(input("Digite o comprimento de uma reta: "));
segundaReta = float(input("Digite o comprimento de uma reta: "));
terceiraReta = float(input("Digite o comprimento de uma reta: "));

if primeiraReta < (segundaReta + terceiraReta) and segundaReta < (primeiraReta + terceiraReta) and terceiraReta < (primeiraReta + segundaReta):
    print("Pode formar um triângulo");

else:
    print("Não pode formar um triângulo");