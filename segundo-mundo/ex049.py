# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

numero = int(input("Digite um número: "));

tabuada = 0;

print(F"-=-=-=TABUADA DO {numero}-=-=-=");

for tabuada in range(0, 10):
    tabuada+=1;
    print(f"{numero} x {tabuada} = {numero*tabuada}");