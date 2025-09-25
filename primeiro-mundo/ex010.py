# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input("Quanto dinheiro você tem? "));

dolares = dinheiro * 5.36;

print(f"Com R$ {dinheiro:.2f} é possível comprar {dolares:.2f} dólares");