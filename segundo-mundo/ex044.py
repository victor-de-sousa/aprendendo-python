# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valorProduto = float(input("Digite o valor do produto: "));
condicaoPagamento = int(input("""Escolha uma das condições de pagamento abaixo: 
    0 - À vista dinheiro/cheque: 10% de desconto
    1 - À vista no cartão: 5% de desconto
    2 - Em até 2x no cartão: preço formal
    3 - 3x ou mais no cartão: 20% de juros """));


if condicaoPagamento < 4:
    
    if condicaoPagamento == 0:
        desconto = valorProduto * 0.9;
        print(f"Valor à ser pago é de: R$ {desconto:.2f}");

    elif condicaoPagamento == 1:
        desconto = valorProduto * 0.95;
        print(f"Valor à ser pago é de: R$ {desconto:.2f}");
    
    elif condicaoPagamento == 2:
        print(f"Valor à ser pago é de: R$ {valorProduto:.2f}");
    
    else:
        juros = valorProduto * 1.2;
        print(f"Valor à ser pago é de: R$ {juros:.2f}");

else:
    print("Valor inserido inválido.");
