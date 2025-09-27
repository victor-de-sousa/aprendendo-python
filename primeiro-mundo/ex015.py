# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quilometros = float(input("Insira a quantidade de quilômetros percorridos: "));
dias = int(input("Insira a quantidade de dias que ele foi alugado: "));

preco = (60 * dias) + (0.15 * quilometros);

print(f"Você deverá pagar R$ {preco:.2f}");
