saldo = 0
saque_max = 3
depositos_realizados = list()


def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print("Deposito realizado com sucesso!")
        depositos_realizados.append(valor)

    else:
        print("Deposito não realizado")


def sacar(valor):
    global saldo
    global saque_max
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado com sucesso!")
        depositos_realizados.append(-valor)
        saque_max -= 1
    else:
        print("Saque nao realizado")


def extrato():
    for depositos in depositos_realizados:
        if depositos > 0:
            print(f"Deposito realidado no valor de: {depositos}\n")
        else:
            print(
                f"Saque realizado no valor de {depositos}\n".replace('-', ''))

    print(f"Saldo Atual: R$ {saldo:.2f}")


def menu():
    print("-=" * 30)
    print("""1 - depositar
2 - sacar
3 - extrato
0 - sair""")


while True:
    menu()
    escolha = int(input("Opção: "))
    if escolha == 1:
        valor = int(input("Qual o valor deseja depositar: "))
        depositar(valor)

    elif escolha == 2:
        if saldo > 0:
            if saque_max > 0:
                print(
                    f"Voce tem um limite de 3 saques diario. voce tem atualmente {saque_max} para hoje")

                valor = int(input("Qual o valor que deseja sacar: "))

                if valor >= saldo:
                    print("A Operação falhou! Voce não tem saldo o suficiente")

                if valor <= 500:
                    sacar(valor=valor)

                else:
                    print(
                        "Seu Valor de saque ultrapassou o limite de 500R$. Tente um valor menor")
            else:
                print(
                    "Seu limite de saque diario extorou, aguarde para realizar o saque amanha!")
        else:
            print("Voce não tem saldo em sua conta")

    elif escolha == 3:
        extrato()

    elif escolha == 0:
        print("Saindo")
        break
