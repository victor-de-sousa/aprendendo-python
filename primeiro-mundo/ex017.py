# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import pow, sqrt;

catetoOposto = float(input('Digite o cateto oposto: '));
catetoAdjacente = float(input('Digite o cateto adjacente: '));

# a² = b² + c²

hipotenusa = sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2));

print(f"A hipotenusa do cateto oposto {catetoOposto} e do cateto adjacente {catetoAdjacente} é {hipotenusa}");
