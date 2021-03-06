# #!/usr/bin/python3

# '''
#     DESAFIO!!!
#     1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
#     2) Agora faca sem utilizar uma terceira variavel temporaria.
#     OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
# '''

# # Funcoes

# # Define a funcao


# def sum(x=3, y=5):
#     print("x: " + str(x))
#     print("y: " + str(y))
#     return x + y


# # Chamada simples de funcao
# x = 1
# y = 2
# z = sum(x, y)
# print(z)

# # Chamada de funcao com parametro sem ordem
# z = sum(y=10, x=13)
# print(z)

# # Utiliza valor padrao dos parametros
# z = sum()
# print(z)

# # PACKING E UNPACKING
# # Atribuicao para mais de uma variável
# a, b = x, y
# print(f'a: {a}, b:{b}')

# list = [1, 2, 3]
# a, b, c = list
# print(f'a: {a}, b:{b}, c:{c}')

# # Ignorando um valor
# a, b, _ = list
# print(f'a: {a}, b:{b},')

# # Multiplos valores (*)
# a, *resto = list
# print(f'a: {a}, resto: {resto}')

# # troca de valores
# a, b = b, a
# print(f'a: {a}, b:{b}')


# # CONDICIONAIS

# temperature = 4
# if temperature <= 0:
#     print('Solido')
# elif temperature > 0 and temperature < 100:
#     print('Liquido')
# else:
#     print('Gasoso')

# # Notacao matematica
# if 0 < temperature < 100:
#     print('Liquido')


# # Operador ternario
# # var = resultado_condicao_verdadeitra if condicao else resultado_condicao_false
# valor = 4
# positivo = True if valor > 0 else False
# print(positivo)


###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais.
# Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
print('1) Crie uma funcao que receba duas listas e verifique se elas são iguais.\n'
      'Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.')


def verifica_listas(lista1, lista2):
    if lista1 == lista2:
        return True
    else:
        return False


lista1 = ['texto lista', 1, 2]
lista2 = ['texto lista', 1, 2]
print(verifica_listas(lista1, lista2))
lista1 = ['texto lista 1', 1, 2]
lista2 = ['texto lista 2', 1, 2]
print(verifica_listas(lista1, lista2))

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas.
# Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
print('\n2) Crie uma funcao que verifica se duas strings são palindromes perfeitas.\n'
      'Faca as "limpeza"/sanitizacao necessarias.  Retorne True ou False.')


def verifica_strings(string1, string2):
    string1 = string1.replace(' ', '')
    string2 = string2.replace(' ', '')

    if(string1.lower()[::-1] == string2.lower()):
        return True
    else:
        return False


string1 = 'Luz azul'
string2 = 'luza zul'
print(verifica_strings(string1, string2))
string1 = 'foca azul'
string2 = 'foca verde'
print(verifica_strings(string1, string2))

# OBS.: Utilize apenas o que foi estudado ate agora
