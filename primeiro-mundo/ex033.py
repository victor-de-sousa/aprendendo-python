# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

primeiroNumero = int(input("Digite um número inteiro: "));
segundoNumero = int(input("Digite um número inteiro: "));
terceiroNumero = int(input("Digite um número inteiro: "));

if primeiroNumero > segundoNumero and primeiroNumero > terceiroNumero:
    if segundoNumero > terceiroNumero:
        print(f"O número {primeiroNumero} é o maior e o número {terceiroNumero} é o menor.");
    else:
        print(f"O número {primeiroNumero} é o maior e o número {segundoNumero} é o menor.");

elif segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    if primeiroNumero > terceiroNumero:
        print(f"O número {segundoNumero} é o maior e o número {terceiroNumero} é o menor.")
    else:
        print(f"O número {segundoNumero} é o maior e o número {primeiroNumero} é o menor.")

elif terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
    if primeiroNumero > segundoNumero:
        print(f"O número {terceiroNumero} é o maior e o número {segundoNumero} é o menor.")
    else:
        print(f"O número {terceiroNumero} é o maior e o número {primeiroNumero} é o menor.")

else:
    print("Você digitou valores iguais, tente novamente.");