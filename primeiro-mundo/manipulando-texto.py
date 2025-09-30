# Fatiamento
# - > frase[9] para mostrar apenas o nono caractere da frase;
# - > frase[9:13] ele vai mostrar do caractere 9 até o caractere 12, mesmo sendo 13 o caractere que será mostrado vai ser um a menos do que o número que você colocou; 
# - > frase[9:21:2] - O 2 seria para pular de 2 em 2 caracteres;
# - > frase[:5] - ele vai mostrar do 1 até o 4 caractere, assim como no exemplo frase[9:13], porém seria como fosse utilizado apenas o frase[:13];
# - > Esse é o contrário do anterior, frase[15:], ele pega apenas os número que estão do 15 até o caractere final;
# - > frase[9::3] - ele vai começar do 9 caractere e vai pulando de 3 em três;

# Análise

# - > len() - Mostra a quantidade de caracteres que há em uma string;

# - > .count('[algum-caractere]') - Conta a quantidade de caracteres em uma string iguais aos que você especifícou.;
# - > .count('[algum-caractere], 0, 13') - Igual o outro, porém agora ele contará apenas do 0 até o 12 caractere;

# - > .find('[algum-texto]') - Ele acha em que posição o [algum-texto] que você digitou começa. E caso não haja esse texto na string ele retornará -1;

# - > '[palavra]' in frase - Ele retorna true caso exista a string (palavra) dentro de frase, e retorna false caso não exista.

# Transformação

# frase.replace('[palavra-frase]', 'Familia') - > Ele substitui a [palavra-frase] da variável frase por Família;
# frase.upper() - > Coloca toda a frase em maiúsculo; 
# frase.lower() - > Coloca toda a frase em minúsculo;
# frase.capitalize() - > Capitaliza a frase, ou seja, a primeira letra da frase se torna maiúscula e o que restou se torna minúsculo;
# frase.title() - > Coloca todas as primeiras letras das palavras que estão divididas por um espaço em branco em maiúsculo;
# frase.strip() - > Tira todos os espaços em branco após e antes da string, por exemplo, '     Família    ', após o frase.strip() ficaria 'Família';
# frase.rstrip() - > Tira os espaços em branco que estão após a string, por exemplo, '     Família    ', após o frase.strip() ficaria '     Família';
# frase.lstrip() - > Tira os espaços em branco que estão antes da string, por exemplo, '     Família    ', após o frase.strip() ficaria 'Família    ';

# Divisão

# frase.split() - > Onde houver espaços dividindo a frase, ele cria divisões e assim cada palavra terá uma posição específica, não mais a letra.

# Junção 

# - > '-'.join(frase) - > Onde houver espaço ele coloca o tracinho, por exemplo, 'Banana Abacate Morango' ficaria assim após o '-'.join(frase) - 'Banana-Abacate-Morango;

# Três aspas duplas (""")

# print("Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos,
#  e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. 
#  Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou 
#  na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de 
#  editoração eletrônica como Aldus PageMaker.")

# Este print daria erro se fosse impresso, por isso nós usaremos """, para que a divisão de linhas do print não dê erro; 

print("""Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos,
e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. 
Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou 
na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de 
editoração eletrônica como Aldus PageMaker.""")

