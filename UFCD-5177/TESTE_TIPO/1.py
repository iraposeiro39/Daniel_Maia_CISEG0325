#!/bin/python3
#
# Init Vars

def primos(x):
    if x <= 1:
        return "Não"
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return "Não"
    return "Sim"

def perfeito(x):
    sum_div = 0
    for i in range(1, x):
        if x % i == 0:
            sum_div += i
    if sum_div == x:
        return "Sim"
    return "Não"

def par_impar(x):
    if x % 2 == 0:
        return "Par"
    else:
        return "Impar"

def divisores(x):
    num = 0
    for i in range(1, x+1):
        if x % i == 0:
            num += 1
    return num

def soma(x, y):
    print(f"{x} + {y} = {x + y}")

def subtracao(x, y):
    print(f"{x} - {y} = {x - y}")

def multiplicacao(x, y):
    print(f"{x} * {y} = {x * y}")

def divisao(x, y):
    print(f"{x} / {y} = {x / y}")

def numeros():
    lista = []
    count = 1
    while count <= 50:
        print("Insira um valor entre 1 e 1000, limite de 50 ('stop' para parar)")
        valor = input(f"nº{count}> ")
        if valor == "stop":
            break
        elif int(valor) < 1 or int(valor) > 1000:
            print("Valor Inválido! Tem de ser um número entre 1 e 1000")
        else:
            count += 1
            lista.append(int(valor))

    count1 = 0
    list_count = 0
    while list_count < len(lista):
        if count1 == 10:
            while True:
                opt = input("Deseja Continuar? (y/n): ")
                match opt:
                    case "y":
                        count1 = 0
                        break
                    case "n":
                        return
        else:
            print(f"\n===! nª{list_count + 1}: {lista[list_count]} !===")
            print(f"Número Primo: {primos(lista[list_count])}")
            print(f"Número Perfeito: {perfeito(lista[list_count])}")
            print(f"Número Par ou Impar: {par_impar(lista[list_count])}")
            print(f"Divisores: {divisores(lista[list_count])}")
            list_count += 1
            count1 += 1
    return

def calc():
    while True:
        num1 = int(input("Insira o 1º num: "))
        if int(num1) < 1 or int(num1) > 1000:
            print("Valor Inválido! Tem de ser um número entre 1 e 1000")
        else:
            break
    while True:
        num2 = int(input("Insira o 2º num: "))
        if int(num2) < 1 or int(num2) > 1000:
            print("Valor Inválido! Tem de ser um número entre 1 e 1000")
        else:
            break
    # Operações
    print("\nQue tipo de operação queres fazer?")
    print("1) Soma")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    while True:
        opt = int(input("> "))
        match opt:
            case 1:
                soma(num1, num2)
                return
            case 2:
                subtracao(num1, num2)
                return
            case 3:
                multiplicacao(num1, num2)
                return
            case 4:
                divisao(num1, num2)
                return
            case _:
                print("Valor inválido!")

def main():
    while True:
        print("\n= Teste Tipo 1 =")
        print("1) Ver números")
        print("2) Calculadora")
        print("3) Sair do programa")
        opt = int(input("> "))
        match opt:
            case 1:
                numeros()
            case 2:
                calc()
            case 3:
                print("Bye!")
                return 0

main()
