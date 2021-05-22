###
# Exercicios
###

# Usando a lista: ['a','b','c']
lista = ['a', 'b', 'c']


# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']
print('1) Faca um loop dentro de uma funcao que irah retornar: ["A","B"","C"]')


def loop(lista):
    for i, letra in enumerate(lista):
        lista[i] = letra.upper()

    return lista


lista = loop(lista)
print(f'{lista}')

# Usando a lista: [0, 1, 7, 4, 5]
lista = [0, 1, 7, 4, 5]


# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas.
# A funcao deve receber a lista como parametro.
print('\n2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas.'
      'A funcao deve receber a lista como parametro.')


def loop2(lista):
    soma = 0

    for valor in lista:
        soma += valor

    return soma


print(f'{loop2(lista)}')


# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da
# lista recebida
print('\n3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares'
      'da lista recebida')


def apenas_impares(lista):
    return[valor for valor in lista if valor % 2 != 0]


print(f'{apenas_impares(lista)}')

# usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
# incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
# ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
# voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
# proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
string = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor '
          'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
          'exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor '
          'in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur '
          'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id '
          'est laborum.')
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list
# comprehension e depois usando list comprehension.
print('\n4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list'
      'comprehension e depois usando list comprehension.')

string = string.split()
soma_maiores_que_5 = 0

for palavra in string:
    if len(palavra) >= 5:
        soma_maiores_que_5 += 1

print(f'Usando for: {soma_maiores_que_5} palavras')

palavras = []
palavras = [palavra for palavra in string if len(palavra) >= 5]
print(f'Usando comprehension: {len(palavras)} palavras')

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
print('\n5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100')
multiplos_de_3 = [valor for valor in range(0, 100) if valor % 3 == 0]
print(multiplos_de_3)


# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula
# else do for
print('\n6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a '
      'clausula else do for')


def encontra_primos():
    primos = []
    for i in range(2, 10):
        primos.append(i)
        for y in range(2, i):
            if i % y == 0 and i != y:
                primos.remove(i)
                break

    return primos


print(f'Números primos: {encontra_primos()}')
