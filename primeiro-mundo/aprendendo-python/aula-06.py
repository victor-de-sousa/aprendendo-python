# primeiroNumero = int(input('Digite um número: '));
# segundoNumero = int(input('Digite um número: '));
# soma = primeiroNumero + segundoNumero;

# # print("A soma entre {} e {} vale: {}".format(primeiroNumero, segundoNumero, soma));

# numero = input('Digite um número: ');
# print(numero.isnumeric());
# print(numero.isalpha);
# print(numero.isalnum());
# print(numero.isupper());
# print(numero.islower());
# print(type(numero));

# # int, float, bool, str    

# Acima está o que eu fiz enquanto assistia a aula

# ___---_-_-___--_----__ DESAFIO 03 _--_---___--_--___--_--___

# primeiroNumero = float(input('Digite um número: '));
# segundoNumero = float(input('Digite um número: '));

# soma = primeiroNumero + segundoNumero;

# print('A soma entre {} e {} é igual à {}'.format(primeiroNumero, segundoNumero, soma));

#  ___---_-_-___--_----__ DESAFIO 04 _--_---___--_--___--_--___

digitado = input('Digite algo: ');

print('Você digitou {}'.format(digitado));
print('O que você digitou é do tipo primitivo {}'.format(type(digitado)));
print('O que você digitou é composto por números? {}'.format(digitado.isnumeric()));
print('O que você digitou é composto por letras? {}'.format(digitado.isalpha()));
print('O que você digitou é um espaço em branco? {}'.format(digitado.isspace()));
print('O que você digitou é composto por apenas letras maiúsculas? {}'.format(digitado.isupper()));
print('O que você digitou é composto por apenas letras minúsculas? {}'.format(digitado.islower()));
