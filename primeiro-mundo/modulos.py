# =-=-=-=-= Módulo -=-=-=-=-

# Para importar um módulo, usamos:
# import [módulo]
# Exemplo: 
# import math

# ----------------------------------------------------------------------

# Para importar algo em específico
# From [modulo] import [funcionalidade-do-modulo]
# Exemplo: 
# from math import sqrt (importa raiz quadrada do módulo math)

# Quando se importa algo de uma biblioteca, não é necessário usar [modulo].[funcionalidade](), podemos usar apenas [funcionalidade]();

# Exemplo com raiz quadrada:
# Antes -> Math.sqrt(numero);
# Depois -> sqrt(numero);

# =-=-=-=-=-=-=-= Prática =-=-=-=-=-=-=-=-=-=-=

# -=-=-=-= Módulo Math -=-=-=-=-=-

# from math import sqrt, trunc;

# numero = float(input("Digite um valor qualquer: "));

# raizQuadrada = trunc(sqrt(numero));

# print(f"A raiz quadrada de {numero} é igual a {raizQuadrada}");

# -=-=-=-= Módulo Random e Emoji -=-=-=-=-=-

# Foi usado o comando "python -m pip install emoji --upgrade" para instalar o módulo emoji no sistema  

import random

import emoji

numero = random.randint(1, 10);

print(numero, emoji.emojize(":thumbs_up:"));