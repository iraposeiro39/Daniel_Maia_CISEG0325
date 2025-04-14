#!/bin/python3
# Teste Final 2: Elabore uma base de dados de clientes de uma fábrica de materiais.
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por
# eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ).
# Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%,
# se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%.
# O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível
# busca direta por número de cliente. 5v.
# O programa deve conter (Estruturas 3v, funções .5v, Vetores .4v, apontadores .3v). 2 H J
#
def calcular_divida_final(compra):
    if 100 <= compra < 200:
        desconto = 0.05
    elif 200 <= compra < 500:
        desconto = 0.10
    elif compra >= 500:
        desconto = 0.15
    else:
        desconto = 0.0
    return compra * (1 - desconto)

def validar_string(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        else:
            print("Entrada inválida. Tente novamente.")

def validar_telefone():
    while True:
        tel = input("Telefone (9 dígitos): ").strip()
        if tel.isdigit() and len(tel) == 9:
            return tel
        else:
            print("Telefone inválido. Deve ter 9 dígitos.")

def validar_nif():
    while True:
        nif = input("NIF (9 dígitos): ").strip()
        if nif.isdigit() and len(nif) == 9:
            return nif
        else:
            print("NIF inválido. Deve ter 9 dígitos.")

def validar_compra():
    while True:
        try:
            compra = float(input("Valor da compra (€): "))
            if compra >= 0:
                return compra
            else:
                print("O valor da compra não pode ser negativo.")
        except ValueError:
            print("Valor inválido. Insira um número.")

def inserir_cliente(clientes, proximo_numero):
    print("\n--- Inserir Novo Cliente ---")
    nome = validar_string("Nome do cliente: ")
    morada = validar_string("Morada: ")
    tel = validar_telefone()
    nif = validar_nif()
    compra = validar_compra()
    divfin = calcular_divida_final(compra)

    cliente = {
        "numcli": proximo_numero,
        "nomcli": nome,
        "morada": morada,
        "tel": tel,
        "nif": nif,
        "compra": compra,
        "divfin": divfin
    }

    clientes.append(cliente)
    print(f"Cliente {nome} inserido com sucesso!\n")
    return proximo_numero + 1

def mostrar_cliente(cliente):
    print(f"Número do Cliente: {cliente['numcli']}")
    print(f"Nome: {cliente['nomcli']}")
    print(f"Morada: {cliente['morada']}")
    print(f"Telefone: {cliente['tel']}")
    print(f"NIF: {cliente['nif']}")
    print(f"Compra: {cliente['compra']:.2f} €")
    print(f"Dívida Final (após desconto): {cliente['divfin']:.2f} €")

def listar_clientes(clientes):
    if not clientes:
        print("\nNenhum cliente registado.\n")
        return

    print("\n--- Lista de Clientes ---\n")
    for cliente in clientes:
        mostrar_cliente(cliente)
        input("\nPrima ENTER para ver o próximo cliente...\n")

def buscar_cliente(clientes):
    try:
        num = int(input("Digite o número do cliente a buscar: "))
        for cliente in clientes:
            if cliente["numcli"] == num:
                print("\nCliente encontrado:\n")
                mostrar_cliente(cliente)
                return
        print("\nCliente não encontrado.\n")
    except ValueError:
        print("Número inválido.")

def menu():
    clientes = []
    proximo_numero = 1

    while True:
        print("\n====== Menu ======")
        print("1. Inserir Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente por Número")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            proximo_numero = inserir_cliente(clientes, proximo_numero)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            buscar_cliente(clientes)
        elif opcao == "4":
            print("A sair do programa. Obrigado!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

menu()
