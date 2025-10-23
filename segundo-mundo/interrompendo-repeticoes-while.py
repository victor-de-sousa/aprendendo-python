# Laços de repetição (Parte 3)

# contador = 1
# while contador <= 10:
#     print(contador, '->', end=' ');
#     contador += 1;

# print('Acabou');

# Quando colocamos True no lugar de 'contador <= 10', faríamos um laço de repetição infinito;

# contador = 1
# while True:
#     print(contador, '->', end=' ');
#     contador += 1;

# print('Acabou');

# Porém podemos fazer esse laço não se repetir infinitamente, com o BREAK;

# contador = 1
# while True:
#     print(contador, '->', end=' ');
#     contador += 1;
#     if contador == 10:
#         break;

# print('Acabou');