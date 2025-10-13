# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salarioFuncionario = float(input("Digite o salário do funcionário: "));

if salarioFuncionario > 1250.00:
    aumento = salarioFuncionario * 1.1;
    print(f"O novo salário do funcionário é: R$ {aumento:.2f}"); 

else:
    aumento = salarioFuncionario * 1.15;
    print(f"O novo salário do funcionário é: R$ {aumento:.2f}"); 
