# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input("Digite uma frase qualquer: "));

semEspacos = frase.replace(" ", "");

aoContrario = semEspacos[::-1];

if semEspacos == aoContrario:
    print("Essa frase é um palíndromo.");
else:
    print("Essa frase não é um palíndromo")
