#!/bin/python3
# Escreva um programa que aceite a entrada de primeiro e último nome e valide se os mesmos nomes estão corretos,
# (Exemplo de nome correto: Timóteo Amaro, primeira Letra de cada nome GRANDE o resto pequeno considerar
# o uso de entoação portuguesa (´ ` ~ ^) uso de tabela ASCII) O programa deve parar de inserir nomes quando
# o utilizador assim o desejar. Ainda deve ter a opção de listar por ordem de primeiro nome e último nome.
#
# Exemplo de lista por Primeiro nome:
# João Messias
# Mário Silva
# Paulo Lima
#
# Último nome:
# Paulo Lima
# João Messias
# Mário Silva
#
# (Usar a tabela ASCII para ordenar obrigatório.)
# O programa deve também manter a idade de cada pessoa introduzida e permitir apagar nomes por primeiro
# ou último validando e informando se existe o nome na lista e apagando a idade e nome correspondente.
# Funções permitidas (adicionar na lista, remover da lista, ord , chr)
#
# A-Z = 65 - 90
# a-z = 97 - 122
#
# lista = ["Anabela", "Xupada", "Zeel", "Carlos", "Portugal", "Beatrix"]
# tmp = 0

# for i in range(len(lista)):
#     for j in range(len(lista)-1):
#         if ord(lista[j][0]) > ord(lista[j+1][0]):
#             tmp = lista[j]
#             lista[j] = lista[j+1]
#             lista[j+1] = tmp

lista_nomes = []
tmp = 0

while True:
    name = input("Insira um nome (parar com 'sair'): ")
    if name == "sair":
        break
    val = 0
    for i in range(len(name)):
        if name[i] == " ":
            break
        else:
            val += 1
    lista_nomes.append([name[:val], name[val+1:]])

    # Bubble Sort dos nomes
    for i in range(len(lista_nomes)):
        for j in range(len(lista_nomes)-1):
            if ord(lista_nomes[j][0][0]) > ord(lista_nomes[j+1][0][0]):
                tmp = lista_nomes[j]
                lista_nomes[j] = lista_nomes[j+1]
                lista_nomes[j+1] = tmp

    print(lista_nomes)
