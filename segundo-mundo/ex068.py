# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# =-=-=-=-=-=-=-

# VAMOS JOGAR PAR OU ÍMPAR

# =-=-=-=-=-=-=-

# Entrada

# Diga um valor: 6

# Par ou ímpar? [P/I];

# Saída

# -----------

# Você jogou 6 e o computador 10. Total de 16 DEU PAR

# -----------

# Você PERDEU!

# =-=-=-=-=-=-=-

# GAME OVER! Você venceu 0 vezes.

from random import randint;


print("""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n
    VAMOS JOGAR PAR OU ÍMPAR\n
=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-\n
""");

perdeu = False;
escolha = '';
numero = -1;
vitoria = soma = par = impar = 0;

while perdeu == False:
    computador = randint(1, 10);
    while numero < 0 or numero > 10:
        numero = int(input("Diga um valor: "));
    while escolha != 'P' and escolha != 'I':
        escolha = str(input("Par ou ímpar? [P/I] "));

    soma = computador + numero; 

    if soma % 2 == 0:
        print(f"\n-------------\nVocê jogou {numero} e o computador {computador}. Total de {soma} DEU PAR\n-------------\n");
        par += 1;
    else:
        print(f"\n-------------\nVocê jogou {numero} e o computador {computador}. Total de {soma} DEU ÍMPAR\n-------------\n");
        impar += 1;

    if escolha == 'P' and par == 1 or escolha == 'I' and impar == 1:
        print('Você VENCEU!\n\n-------------\n');
        numero = -1;
        escolha = '';
        par = impar = 0;
        vitoria += 1;
    else:
        print("Você PERDEU!\n\n=-=-=-=-=-=-=-\n");
        break;

print(f"GAME OVER! Você venceu {vitoria} vezes");


