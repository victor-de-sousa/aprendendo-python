# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input("Digite a distância em quilômetros percorrida: "));

if distancia <= 200:
    print(f"Você pagará R${(distancia * 0.5):.2f}");
else:
    print(f"Você pagará R${(distancia * 0.45):.2f}");