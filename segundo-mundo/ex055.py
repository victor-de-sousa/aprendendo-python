# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maiorPeso = 0;
menorPeso = 0;

for quantidade in range(0, 5):
    peso = int(input("Digite o seu peso: "));
    if quantidade == 0:
        menorPeso = peso;
    if maiorPeso < peso:
        maiorPeso = peso;
    elif menorPeso > peso:
        menorPeso = peso;

print(f"""O maior peso inserido foi de: {maiorPeso}
E o menor peso inserido foi de: {menorPeso}""");