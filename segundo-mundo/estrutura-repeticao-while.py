# Estrutura de Repetição While

# Se usa quando não se sabe o limite

# Mesmo resultado, porém usando estruturas de repetição diferentes

# for c in range(1, 10):
#     print(c);
# print("FIM")

# c = 1;
# while c < 10:
#     print(c)
#     c += 1;
# print("FIM")

# Outro exemplo, porém só funciona com while

numero = 1;
decisao = 'S';
par = 0;
impar = 0;


while decisao == 'S':
    numero = int(input("Digite um valor: "));
    decisao = str(input("Quer continuar [S/N] ? ")).upper();
    if numero % 2 == 0:
        par += 1;
    else:
        impar += 1;

print(f"Você digitou {par} número pares, e {impar} números ímpares.");