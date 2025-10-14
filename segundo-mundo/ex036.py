# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Qual o valor da casa? "));
salario = float(input("Qual o seu salário? "));
anos = int(input("Em quantos anos você deseja pagar a casa? "));

prestacaoMensal = (valorCasa / (anos * 12));

if prestacaoMensal > (salario * 0.3):
    print("O empréstimo foi negado");

else:
    print("O empréstimo foi aceito");

