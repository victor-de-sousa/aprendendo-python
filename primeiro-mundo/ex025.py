#  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nomeCompleto = str(input('Digite o seu nome completo: '));

verificador = "SILVA" in nomeCompleto.upper();

print(f"O nome {nomeCompleto} tem Silva? {verificador}");