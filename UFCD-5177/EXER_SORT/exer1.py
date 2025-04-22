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

### Iniciar Variáveis
lista_nomes = []
# Lista de template, para testes:
# lista_nomes = [['Abilio', 'Zacarias', 19], ['Babete', 'Yggdrasil', 22], ['Catarina', 'Xupada', 4]]
tmp = 0
rm = 0

### Funções
# Adicionar nome à lista
def adicionar_lista():
    # Inserir nomes até sair, dividir os mesmos e mete-los na lista
    print("Para parar, insira 'sair'")
    while True:
        # Pede para inserir o nome
        name = input("Insira um nome: ")

        ### VERIFICAÇÃO DO NOME
        # Se for inserida a palavra 'sair', o programa retorna
        if name == "sair":
            return 0

        # Sacar o número de carateres do primeiro nome para dividir os dois nomes
        val = 0
        for i in range(len(name)):
            if name[i] == " ":
                break
            else:
                val += 1

        # Verificar se existem dois nomes
        if " " not in name:
            print("O nome tem de conter dois nomes!")
        # Verificar se as primeiras letras dos dois nomes são Upper Case
        elif ord(name[0]) >= 97 or ord(name[val+1:val+2]) >= 97:
            print("A primeira letra de cada nome tem de ser Upper Case!")
        # Se tudo der certo, continua...
        else:
            idade = int(input("Insira a idade: "))
            # Append do primeiro nome, do ultimo nome e da idade em indexes diferentes
            lista_nomes.append([name[:val], name[val+1:], idade])

# Remove nome da lista
def remover_lista():
    # Se a lista tiver vazia, não faz nada
    if lista_nomes == []:
        print("A lista está vazia!")
        return 1
    else:
        while True:
            rm = input("\nQue nome deseja remover?: ")
            # Percorre a lista para procurar pela sublista com o nome especificado
            for i in range(len(lista_nomes)):
                # Se a palavra tiver na sublista...
                if rm in lista_nomes[i]:
                    # Diz que encontrou e que vai apagar!
                    print(f"Apagado o nome {lista_nomes[i][0]} {lista_nomes[i][1]} com {lista_nomes[i][2]} anos do indice nº{i}")
                    # E apaga
                    lista_nomes.pop(i)
                    return 0
            # Se depois de percorrer todas as sublistas e não encontrar nada:
            print(f"O nome {rm} não existe!")

# Main Loop (menu)
while True:
    print("\n= Exercicio 1 - Sort! =")
    print("1) Adicionar na lista")
    print("2) Mostrar as listas")
    print("3) Apagar na lista")
    print("4) Sair")
    opt = int(input("> "))
    match opt:
        case 1:
            adicionar_lista()
        case 2:
            if lista_nomes == []:
                print("A lista está vazia!")
            else:
                # Menu para determinar o tipo de sort, fosse possivel usar mais funções, era possivel fazer
                # uma função sort que retiraria umas quantas linhas de codigo
                print("\nDesejas ordenar apartir...: ")
                print("1) Primeiro Nome")
                print("2) Ultimo Nome")
                print("3) Idade")
                opt = int(input("> "))
                match opt:
                    case 1:
                        # Bubble Sort do Primeiro Nome
                        for i in range(len(lista_nomes)):
                            for j in range(len(lista_nomes)-1):
                                if ord(lista_nomes[j][0][0]) > ord(lista_nomes[j+1][0][0]):
                                    tmp = lista_nomes[j]
                                    lista_nomes[j] = lista_nomes[j+1]
                                    lista_nomes[j+1] = tmp

                    case 2:
                        # Bubble Sort do Ultimo Nome
                        for i in range(len(lista_nomes)):
                            for j in range(len(lista_nomes)-1):
                                if ord(lista_nomes[j][1][0]) > ord(lista_nomes[j+1][1][0]):
                                    tmp = lista_nomes[j]
                                    lista_nomes[j] = lista_nomes[j+1]
                                    lista_nomes[j+1] = tmp

                    case 3:
                        # Bubble Sort da Idade
                        for i in range(len(lista_nomes)):
                            for j in range(len(lista_nomes)-1):
                                if lista_nomes[j][2] > lista_nomes[j+1][2]:
                                    tmp = lista_nomes[j]
                                    lista_nomes[j] = lista_nomes[j+1]
                                    lista_nomes[j+1] = tmp

                    case _:
                        print("Opção Inválida!")

                print("\n===> Lista de nomes")
                for i in range(len(lista_nomes)):
                    print(f"{lista_nomes[i][0]} {lista_nomes[i][1]} - {lista_nomes[i][2]} anos")
            var = input("\nPrima enter para continuar...")

        case 3:
            remover_lista()
        case 4:
            print("Bye!")
            break
        case _:
            print("Valor Inválido!")
