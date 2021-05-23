###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
print('1) Imprima os metodos disponiveis para uma lista e para uma tupla')
print(f'Métodos para listas: \n{dir(list)}\n')
print(f'Métodos para tuplas: \n{dir(tuple)}\n')

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
print('2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos')


def diferenca_metodos_lista_tupla():
    metodos_lista = dir(list)
    metodos_tupla = dir(tuple)

    metodos_apenas_lista = [
        metodo for metodo in metodos_lista if not metodos_tupla.__contains__(metodo)]
    print(f'Métodos apenas da lista: \n{metodos_apenas_lista}\n')

    metodos_apenas_tupla = [
        metodo for metodo in metodos_tupla if not metodos_lista.__contains__(metodo)]
    print(f'Métodos apenas da tupla: \n{metodos_apenas_tupla}')


diferenca_metodos_lista_tupla()

# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3.
# Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.
print('\n3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3.'
      'Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.')

professor1 = {'id': 42,
              'name': 'Alexandre Abreu',
              'age': 30,
              'state_origin': 'Minas Gerais',
              'courses': [
                  'Inteligência Artificial',
                  'Mineração de Dados',
                  'Programação para Internet I',
                  'Programação para Internet II'
              ]}

professor2 = {'id': 37,
              'name': 'Denilson Barbosa',
              'age': 40,
              'state_origin': 'Paraná',
              'courses': [
                  'Inteligência Artificial',
                  'Banco de Dados I',
                  'Banco de Dados II',
                  'Programação para Internet I',
              ]}

professor3 = dict(id=28, name='Jorge Armino', idade=37)

professor1['coordenadas'] = ('1111', '1212')
professor2['coordenadas'] = ('1313', '1414')
professor3['coordenadas'] = ('1515', '1616')

print(f'Coordenadas professor1: {professor1["coordenadas"]}')
print(f'Coordenadas professor2: {professor2["coordenadas"]}')
print(f'Coordenadas professor3: {professor3["coordenadas"]}')
