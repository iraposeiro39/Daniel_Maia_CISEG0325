#!/bin/python3
# Class para criar uma pessoa
class Pessoa:
    def __init__(self,nome,apelido,idade):
        self.nome = nome
        self.apelido = apelido
        self.idade = idade
    def renovar_idade(self,idade):
        self.idade = idade

lista = []
length = int(input("Quantas pessoas queres adicionar?: "))
for i in range(1, length+1):
    print(f"== Pessoa nº{i}: ==")
    x = input("Insira o seu nome: ")
    y = input("Insira o seu apelido: ")
    z = int(input("Insira a sua idade: "))
    pessoa = Pessoa(x, y, z)
    lista.append(pessoa)

for i in range(len(lista)):
    print(f"\n== Pessoa nº{i} ==")
    print(f"Nome: {lista[i].nome}")
    print(f"Apelido: {lista[i].apelido}")
    print(f"Idade: {lista[i].idade}")
