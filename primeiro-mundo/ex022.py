# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nomeCompleto = str(input('Digite o seu nome completo: '));

semEspacos = nomeCompleto.replace(" ", "");
primeiroNome = nomeCompleto.split();

print(f"""Seu nome é: {nomeCompleto}\n
- Com letras maíscúlas: {nomeCompleto.upper()}
- Com letras minúsculas: {nomeCompleto.lower()}
- Quantidade de letras: {len(semEspacos)}
- Quantas letras no primeiro nome: {len(primeiroNome[0])}""");