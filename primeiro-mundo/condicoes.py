# --------- Condições ---------

# tempoCarro = int(input("Quantos anos tem seu carro: "));
# if tempoCarro <= 3:
#   print('Carro Novo');
# else:
#   print('Carro Velho');
# print('--FIM--');

# - Esse programa pode ser reescrito da seguinte forma:

# tempoCarro = int(input("Quantos anos tem seu carro: "));
# print('Carro Novo' if tempoCarro <= 3 else 'Carro Velho');
# print('--FIM--');

# --------- Prática ---------

# 01

# import emoji;

# nomeCompleto = str(input("Qual seu nome completo? "));
# dataNascimento = str(input("Qual sua data de nascimento? "));

# if nomeCompleto == "Maria Fernanda da Rocha Valencio de Souza":
#     if dataNascimento == "15/12/2008":
#         print(emoji.emojize("\nOiiii minha princesinha maravihermosa :two_hearts:"));

# else:
#     print(f'Olá bom dia, {nomeCompleto}');

# 02

# primeiraNota = float(input("Digite a primeira nota: "));
# segundaNota = float(input("Digite a segunda nota: "));
# media = (primeiraNota + segundaNota) / 2;

# print(f"A sua média foi de: {media:1}");


# #   if media < 7:
# #       print("Sua média foi ruim.");

# #   else:
# #       print("PARABÉNS, você tirou uma boa média!");

# Outra forma seria:

# print(f"Sua média foi ruim." if media < 7 else "PARABÉNS, você tirou uma boa média!");


