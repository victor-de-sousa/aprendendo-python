# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = float(input('Digite um valor qualquer: '));

dobro = numero * 2;
triplo = numero * 3;
raizQuadrada = numero ** (1/2);

print(f'O número {numero:.2f}:\nO dobro deste número é: {dobro:.2f}\nO triplo deste número é: {triplo:.2f}\nA raiz quadrada deste número é {raizQuadrada:.1f}');
