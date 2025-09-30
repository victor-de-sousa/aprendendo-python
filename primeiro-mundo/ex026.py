#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = (str(input('Digite uma frase: ')));

fraseMaiuscula = frase.upper();

quantidadeVezes = fraseMaiuscula.count('A');

primeiraPosicao = fraseMaiuscula.find('A');

ultimaPosicao = fraseMaiuscula.rfind('A');


print(f"""Na frase: {frase}
A letra A aparece cerca de: {quantidadeVezes} vezes
Ela aparece pela primeira vez na posição: {primeiraPosicao}
Ela aparece pela última vez na posição: {ultimaPosicao}""");