# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = [];

for quantidade in range(0, 5):
    peso = int(input("Digite o seu peso: "));
    pesos.append(peso);

pesos.sort();

print(f"""O maior peso lido foi: {pesos[-1]}
O menor peso lido foi {pesos[0]}"""); 