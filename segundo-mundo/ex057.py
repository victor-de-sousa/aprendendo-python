# Faça um programa que leia o sexo de um pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Insira o seu sexo: "));

while sexo != 'M' or sexo != 'F':
    sexo = str(input("Insira o seu sexo: novamente: "));

print(f"O seu sexo é: {sexo}");