from datetime import datetime

saldo = 0
saque_max = 3
transacao_diaria = 10
transacao_realizados = ''

def depositar(valor):
    global transacao_realizados
    global saldo
    global transacao_diaria
    if transacao_diaria > 0:
        if valor > 0:
            saldo += valor
            hora = datetime.now().strftime("%H:%M:%S")
            data = datetime.now().strftime("%d/%m/%Y")
            print("Deposito realizado com sucesso!")
            transacao_diaria -= 1
            print(f"Voce ainda pode fazer {transacao_diaria} transações hoje")
            transacao_realizados += f"Data: {data} Horario: {hora}: Deposito: {valor:.2f}\n"
        else:
            print("Deposito não realizado")
    else:
        print("Seu limite de transação diaria acabou, aguarde o proximo dia")


def sacar(valor):
    global transacao_realizados
    global transacao_diaria
    global saldo
    global saque_max
    if transacao_diaria > 0:
        if saldo >= valor:
            saldo -= valor
            hora = datetime.now().strftime("%H:%M:%S")
            data = datetime.now().strftime("%d/%m/%Y")
            print("Saque realizado com sucesso!")
            transacao_diaria -= 1
            print(f"Voce ainda pode fazer {transacao_diaria} transações hoje")
            transacao_realizados += f"Data: {data} Horario: {hora}: Saque: {valor:.2f}\n"
            saque_max -= 1
        else:
            print("Saque nao realizado")
    else:
        print("Seu limite de transação diaria acabou, aguarde o proximo dia")


def extrato():
    print("-=" * 20)
    print(transacao_realizados)
    print()
    print()
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("-=" * 20)


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
                elif valor < 0:
                    print("A Operação falhou! O valor informado e invalido.")

                elif valor <= 500:
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
