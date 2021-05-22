# #!/usr/bin/python3

# '''
#     DESAFIO!!!
#     Implemente um algoritmo para inverter a ordem de uma string em sua
#     linguagem de programacao favorita. Nao use funcoes/metodos prontos.
# '''

# # STRINGS
# # https://docs.python.org/3/tutorial/introduction.html#strings

# msg = 'Minimal Techno Tripping'
# size = len(msg)
# print('Tamanho de msg:')
# print(size)

# # Converter para string
# s = str(42)
# print(s)

# s = 'I like you'
# print(s)

# # Examine as strings colocando prints
# s2 = s[0]  # retorna 'I'

# s2 = len(s)  # retorna 10

# # Como jah fizemos com as listas
# s2 = s[0:7]  # retorna 'I like '

# s2 = s[6:]  # retorna ' you'

# s2 = s[-1]  # retorna 'u'


# # concatenar strings
# s3 = 'The meaning of life is'
# s4 = '42'
# s5 = s3 + ' ' + s4       # retorna 'The meaning of life is 42'
# s5 = s3 + ' ' + str(42)  # same thing

# # split a string into a list of substrings separated by a delimiter

# s = 'Anything you want it to be'
# s.split(' ')        # retorna ['Anything', 'you', 'want', 'it', 'to', 'be']
# s.split()           # idem


# # Entrada via teclado (caracter de escape -> '\')
# print('What\'s your name?')
# nome = input()
# sobrenome = 'Abreu'
# print('Hi, ' + nome)
# print('Hi,', nome)

# # Formatacao com o metodo format
# msg = 'Hi, {} {}!'.format(sobrenome, nome)
# print(msg)
# msg = f'Hi, {sobrenome} {nome}!'
# print(msg)


# # Inverter a string
# string = 'Hello, my friend!'
# print(string)
# string2 = string[::-1]
# print(string2)

# # Substituir
# cheese_str = 'I like cheese'
# print(cheese_str)
# new_cheese_str = cheese_str.replace('like', 'love')
# print(new_cheese_str)

###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
print('\n1) Extraia o titulo do livro da string')
book1 = book1.split(' by ')
print(book1[0])
book2 = book2.split(' by ')
print(book2[0])
book3 = book3.split(' by ')
print(book3[0])


# 2) Salve o titulo de cada livro em uma variável
print('\n2) Salve o titulo de cada livro em uma variável')
titulo1 = book1[0]
print(titulo1)
titulo2 = book2[0]
print(titulo2)
titulo3 = book3[0]
print(titulo3)

# 3) Quantos caracteres cada título tem?
print('\n3) Quantos caracteres cada título tem?')
print(len(titulo1))
print(len(titulo2))
print(len(titulo3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
print('\n4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}')
print('{} - {}, {}'.format(
    titulo1,
    book1[1].split(',')[0],
    book1[1].split(', ')[1],
))

print('{} - {}, {}'.format(
    titulo2,
    book2[1].split(',')[0],
    book2[1].split(', ')[1],
))

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

print('\n5) Verifique se uma palavra é uma palindrome perfeita.\n')

if palindrome_one == palindrome_one[::-1]:
    print(f'{palindrome_one} é uma palindrome')
else:
    print(f'{palindrome_one} não é uma palindrome')

if palindrome_two.lower() == (palindrome_two[::-1]).lower():
    print(f'{palindrome_two} é uma palindrome')
else:
    print(f'{palindrome_two} não é uma palindrome')

if palindrome_three.replace(' ', '') == (palindrome_three[::-1]).replace(' ', ''):
    print(f'{palindrome_three} é uma palindrome')
else:
    print(f'{palindrome_three} não é uma palindrome')

if palindrome_four.replace(' ', '') == (palindrome_four[::-1]).replace(' ', ''):
    print(f'{palindrome_four} é uma palindrome')
else:
    print(f'{palindrome_four} não é uma palindrome')
