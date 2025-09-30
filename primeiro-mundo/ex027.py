# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nomeCompleto = str(input("Digite o seu nome completo: "));

nomeDividido = nomeCompleto.split();

primeiroNome = nomeDividido[0];

ultimoNome = nomeDividido[-1];

print(f"""O nome completo é: {nomeCompleto};\n
O primeiro nome é: {primeiroNome};
O último nome é: {ultimoNome}.""");