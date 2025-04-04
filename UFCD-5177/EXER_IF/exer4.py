#!/bin/python3
# Exercício 4: Fazer um algoritmo que leia o saldo inicial de cliente do banco e leia também um cheque que entrou
# e ANALISE se o cheque poderá ser descontado ou não, já que este cliente não possui limite.
# Se o cheque não poderá ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo.
#
# Input
saldo = int(input("Insira o seu saldo: "))
cheque = int(input("Insira o valor do cheque: "))

# Logica
if cheque > saldo:
    print("O cheque não pode ser descontado!")
else:
    saldo = saldo-cheque
    print(f"Operacao com sucesso! Saldo atual: {saldo}")
