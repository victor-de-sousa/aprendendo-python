# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input("Digite um ângulo: "));

radianos = radians(angulo)

seno = round(sin(radianos), 1);
cosseno = round(cos(radianos), 1);
tangente = round(tan(radianos), 1);

print(f"O ângulo {angulo}° Possui:\nSeno de: {seno};\nCosseno de {cosseno};\nTangente de: {tangente}")
