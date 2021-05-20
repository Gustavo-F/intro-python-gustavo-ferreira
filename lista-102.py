#!/usr/bin/python3

# LISTS
# https://docs.python.org/3/tutorial/introduction.html#lists

# list slicing [inicio:fim:passo]

weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']

print(weekdays)
print(type(weekdays))

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

print(test)

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat', 'sun']     # concatenar

print(all_days)

# Usando append
days_list = ['mon', 'tues', 'wed', 'thurs', 'fri']
days_list.append('sat')
days_list.append('sun')

print(days_list)
print(days_list == all_days)

list = ['a', 1, 3.14159265359]
print(list)
print(type(list))

# list.reverse()
# print(list)

#########
# Exercicios - Listas
# Faca sem usar loops
#########

# Como selecionar 'wed' pelo indice?
print(days_list[2])

# Como verificar o tipo de 'mon'?
print(type(days_list[0]))

# Como separar 'wed' até 'fri'?
print(days_list[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print(days_list[4])
print(days_list[4:5])

# Qual eh o tamanho dos dias e days_list?
print(len(days_list[0]))  # Refazer
print(len(days_list))    # Refazer

# Como inverter a ordem dos dias?
days_list_inverted = days_list[::-1]
print(days_list_inverted)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
# list[0::1] = 'zero'
# print(list)

# Como limpar list?
print(list.clear)

# Como deletar list?

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list[-1]
list.remove(list[-1])
print(ultimo_elemento)
print(list)
