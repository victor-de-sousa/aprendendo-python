# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

menu = 4;

while menu > 0 and menu < 5:

    if menu == 4:
        primeiroNumero = int(input("Digite um número: "));
        segundoNumero = int(input("Digite um número: "));

    menu = int(input("""Você deseja: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Insira aqui a sua escolha: """));

    print('');

    if menu == 1:
        print(f"A soma entre os dois números é igual à {primeiroNumero + segundoNumero}\n");
    elif menu == 2:
        print(f"A multiplicação entre os dois números é igual à: {primeiroNumero * segundoNumero}\n");
    elif menu == 3:
        if primeiroNumero > segundoNumero:
            print(f"O maior número entre os dois é: {primeiroNumero}\n");
        elif segundoNumero > primeiroNumero:
            print(f"O maior número entre os dois é: {segundoNumero}\n");
        else:
            print(f"Os dois números são iguais.\n");

print("----FIM DO PROGRAMA----");

