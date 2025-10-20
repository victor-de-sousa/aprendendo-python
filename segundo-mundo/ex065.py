# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = 0;
soma = 0;
media = 0;
maior = 0;
menor = 0;

while contador != 10:
    contador+=1;
    numero = int(input("Insira um número para continuar: "));
    soma += numero;
    media += 1;

    if contador == 1:
        menor = numero;

    if numero > maior:
        maior = numero;

    elif numero < menor:
        menor = numero;

    if contador == 10:
        media = soma / media;
        print(f"O maior número é: {maior}");
        print(f"O menor número é: {menor}");
        print(f"A média entre todos os números é igual à {media:.2f}");
        
        continuarUsuario = '';
        
        while continuarUsuario != 'S' and continuarUsuario != 'N':
            continuarUsuario = str(input("Você deseja continuar a digitar valores? [S/N] "));
            
        if continuarUsuario == "S":
            contador = 2;