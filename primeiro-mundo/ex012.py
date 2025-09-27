# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite aqui o preço de um produto: "));

desconto = preco * 0.95;

print(f"O produto caiu de R$ {preco:.2f} para R$ {desconto:.2f} após o desconto!")