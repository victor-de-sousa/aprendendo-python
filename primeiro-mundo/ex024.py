# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite o nome de uma cidade: "));

dividindo = cidade.split();

primeiroNome = dividindo[0];

verificador = "SANTO" in primeiroNome.upper();

print(f"A cidade {cidade} começa com Santo? {verificador}");