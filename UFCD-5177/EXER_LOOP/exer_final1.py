#!/bin/python3
# Teste Final 1: Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1
# (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000,
# e parar de 10 em 10 valores com instrução para parar ou continuar.
# No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada.
# Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo
# introduzido) deve parar de 20 em 20 valores.
#
def primo(var):
    primo = True
    for i in range(2, int(var**0.5) + 1):
        if var % i == 0:
            primo = False
            break
    if primo:
        return True
    else:
        return False

def divisores(var):
    divisores = []
    for i in range(1,var+1):
        if var % i == 0:
            divisores.append(i)
    print(f"Possui {len(divisores)} divisores: {divisores}")


def num_perfeito(var):
    valores = []
    soma = 0
    for i in range(1,var+1):
        if var % i == 0:
            valores.append(i)
            soma = sum(valores)
        if soma == var:
            return True

def numeros():
    while True:
        num = int(input("Insira um valor entre 1 e 30000: "))
        if num >= 1 and num <= 30000:
            for i in range(num, 0, -1):
                print(f"===> Número {i}:")
                if primo(i) and i != 1:
                    print("É Primo!")
                if num_perfeito(i) and i != 1:
                    print("É número perfeito!")
                divisores(i)
                print("")
            break
        else:
            print("Número Inválido!")

def calc():
    num1 = int(input("Insira o 1º valor: "))
    num2 = int(input("Insira o 2º valor: "))
    print("Que operação desejas efetuar?")
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")
    opt = int(input("> "))
    match opt:
        case 1:
            print(f"{num1} + {num2} = {num1+num2}")
        case 2:
            print(f"{num1} - {num2} = {num1-num2}")
        case 3:
            print(f"{num1} * {num2} = {num1*num2}")
        case 4:
            print(f"{num1} / {num2} = {num1/num2}")

def tabuada():
    while True:
        num = int(input("O programa irá efetuar a tabuada de 1 a: "))
        if num >= 1 and num <= 1000:
            for i in range(1, num+1):
                for j in range(1, 11):
                    print(f"{i} * {j} = {i*j}")
            break
        else:
            print("Número Inválido! (Tem de estar entre 1 e 1000)")

def main():
    while True:
        print("=========! Teste Final 1 !=========")
        print("O que deseja fazer?")
        print("1) Números")
        print("2) Calculadora")
        print("3) Tabuada")
        print("4) Sair")
        opt = int(input("> "))
        match opt:
            case 1:
                numeros()
            case 2:
                calc()
            case 3:
                tabuada()
            case 4:
                print("Bye!")
                break

main()
