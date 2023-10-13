'''Fatiamento

frase = Curso em Vídeo Python - 20 caracteres


Para fatiar, usamos
frase[9:13] - que vai pegar os caracteres numero 9 até *12*.
frase[9:13] = 'vide'
para pegar todos os caracteres desejáveis, precisamos informar a proxima string
frase[9:14] = 'video'

outra forma de fatiar, é pulando strings
frase[9:21:2] vai pegar todas as strings do 9 ao 20 e vai apresentar pulando uma casa
frase[9:21:2] = VdoPto

frase[:5] vai pegar todos os caracteres de 0 à 4
frase[:5] = Curso

frase[15:] vai pegar todos os caracteres a partir do caractere 15
frase[15:] = Python

frase[9::3] vai pegar todos os caracteres a partir da casa 9 e apresentar de 3 em 3
frase[9::3] = Veph

Análise

len(frase) - Vai apresentar o número de caracteres que tem na frase
len(frase) = 21 caracteres

frase.count('o') vai contar quantas vezes existem a letra 'o'
frase.count('o') = 3 caracteres

frase.count('o', 0, 13) quantos caracteres 'o' existem entre 0 e 12
frase.count('o', 0, 13) = 1 caractere

frase.find('deo') - vai procurar onde tem 'deo' na lista de caracteres
frase.find('deo') = 11 (que se refere a casa onde começa a sequencia 'deo')

frase.find('Android') - Se você passa uma funcionalidade que não existe, ele te retorna -1
frase.find('Android') = -1

'Curso' in frase - vai retornar valor booleano se existe ou não esse conjunto de strings
'Curso' in frase = True

Transformação

frase.replace('Python', 'Android') - ele vai substituir o conjunto 'Python' por 'Android'

frase.upper() - método para transformar todas os caracteres em maiúsculos

frase.lower() - método para transformar todos os caracteres em minúsculos

frase.capitalize() - vai pegar todas as strings, transformar em minúsculo, exceto o primeiro caractere
frase.capitalize() = Curso em video python

frase.title() - vai transformar todas os primeiros caracteres de cada palavra em maiúsculo
frase.title() = Curso Em Vídeo Python

frase.strip() - vai eliminar todas os espaços vazios na memória em torno da frase e vai realocar os espaços na memória
*exemplo* |   Aprenda Python  | - contém 3 casas vazias no começo e 2 no fim
frase.strip() = |Aprenda Python| (vai manter apenas a casa vazia do espaço entre as palavras)

frase.rstrip() - vai eliminar os espaços vazios apenas da direita
frase.lstrip() - vai eliminar os espaços apenas da esquerda

Divisão

frase.split() - Vai separar toda a cadeia de caracteres da frase, cada palavra vai ser uma caixa de caracteres nova
frase.split() = |Curso| |em| |Vídeo| |Python|

Junção

'-'.join(frase) - Ele vai colocar um '-' nos espaços de cada palavra
'-'.join(frase) = Curso-em-Vídeo-Python

'''