import csv
import tarfile

###
# Exercicios
###

estados_capitais = []
with open('capitais-BR.csv', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for estado_capital in reader:
        estados_capitais.append(estado_capital)

# estado_capital = estados_capitais[0]
# print(estado_capital[0])


# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao.
# Utilize a clausula else no loop implementado.
print('1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao.'
      'Utilize a clausula else no loop implementado.')


def define_default_city(state):
    '''
    Define a capital do estado de origem como city_origin para um professor existente no arquivo. 
    Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.

    Keyword arguments:
        state -- O estado de origem do professor
    '''

    for estado_capital in estados_capitais:
        if state == estado_capital[0]:
            return True
    else:
        return False


print(define_default_city('Pará'))

# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao
# estah robusta o suficiente. Ela deve executar sem erro mesmo que alguns dados estejam faltando.

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao)
# e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo
# lista-cpf.txt.tar.gz primeiro. O algoritmo precisa ser eficiente, nesse caso especifico a melhor a
# melhor complexidade que pode ser acancada é linear. Algoritmos de complexidade quadratica, cubica,
# fatorial, etc. não sao considerados como eficientes pois a complexidade linear eh garantida.
# Como regra geral, se seu algoritmo demorar mais do que alguns segundos, ele, provavelmente,
# nao eh linear.


def qtd_cpf():
    arquivo = tarfile.open('lista-cpf.txt.tar.gz')
    arquivo.extractall()

    cpfs_unicos = []
    i = 0
    with open('lista-cpf.txt', mode='r') as lista_cpf:
        for cpf in lista_cpf:
            if not cpfs_unicos.__contains__(cpf):
                cpfs_unicos.append(cpf)
            i += 1
            print(i)

    print(len(cpfs_unicos))


qtd_cpf()
