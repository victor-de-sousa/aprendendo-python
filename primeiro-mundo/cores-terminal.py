#  =-=-=-=-= Cores no Terminal -=-=-=-=-

# \033[[style:text:background]m

# \033[0;33;44m

# Style:

# 0 - None
# 1 - Bold / Negrito
# 4 - Underline / Sublinhalido
# 7 - Negative - Inverte as configurações

# Text:

# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelho
# 34 - Azul
# 35 - Magenta
# 36 - Ciano
# 37 - Cinza

# Back:

# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelho
# 44 - Azul
# 45 - Magenta
# 46 - Ciano
# 47 - Cinza

# print("\033[7mOlá mundo!\033[m")

elogio = "minha princesa";
cores = {
    'Limpa' : '\033[m',
    'Magenta' : '\033[35m',
    'Magenta-Negrito' : '\033[1;35m',
    'Magenta-Negrito-Sublinhado' : '\033[1;4;35m',

}
print(f"Eu te amo {cores['Magenta-Negrito-Sublinhado']}{elogio}{cores['Limpa']}");
