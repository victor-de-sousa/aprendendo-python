# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

mediaIdade = 0;
idadeHomem = 0;
nomeHomem = "";
mulherAnos = 0;

for pessoa in range(0, 4):
    nome = str(input("Insira o nome de uma pessoa: "));
    idade = int(input("Insira a idade dessa pessoa: "));
    sexo = str(input("Insira o sexo desta pessoa: ").upper());

    mediaIdade = mediaIdade + idade;

    if sexo == "M":
        if idadeHomem < idade:
            idadeHomem = idade;
            nomeHomem = nome;
    elif sexo == "F":
        if idade < 20:
            mulherAnos += 1;

print(f"""A média de idade do grupo é: {mediaIdade/4}
O nome do homem mais velho é: {nomeHomem}
A quantidade de mulheres que tem menos de 20 anos é: {mulherAnos}""");