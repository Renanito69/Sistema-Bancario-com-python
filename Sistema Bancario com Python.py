from datetime import datetime

usuario = list()
cliente = dict()
endereco = dict()
criando_conta_corrente = dict()
conta_corrente = list()
saldo = 0
saque_max = 3
transacao_diaria = 10
transacao_realizados = ''
numeros_contas_usuario = 0


def depositar(valor, saldo, extrato, /):
    global transacao_realizados
    global transacao_diaria
    if transacao_diaria > 0:
        if valor > 0:
            saldo += valor
            hora = datetime.now().strftime("%H:%M:%S")
            data = datetime.now().strftime("%d/%m/%Y")
            print("Deposito realizado com sucesso!")
            transacao_diaria -= 1
            print(f"Voce ainda pode fazer {transacao_diaria} transações hoje")
            extrato += f"Data: {data} Horario: {hora}: Deposito: {valor:.2f}\n"
            return saldo, extrato
        else:
            print("Deposito não realizado")
    else:
        print("Seu limite de transação diaria acabou, aguarde o proximo dia")


def sacar(*, saldo, valor, extrato, numero_saques, limite_saques):
    if numero_saques > 0:
        if saldo >= valor:
            saldo -= valor
            hora = datetime.now().strftime("%H:%M:%S")
            data = datetime.now().strftime("%d/%m/%Y")
            print("Saque realizado com sucesso!")
            numero_saques -= 1
            print(f"Voce ainda pode fazer {numero_saques} transações hoje")
            extrato += f"Data: {data} Horario: {hora}: Saque: {valor:.2f}\n"
            limite_saques -= 1
            return saldo, extrato, numero_saques, limite_saques
        else:
            print("Saque nao realizado")
    else:
        print("Seu limite de transação diaria acabou, aguarde o proximo dia")


def extrato(saldo, *, extrato_atual=transacao_realizados):
    print("-=" * 20)
    print(extrato_atual if extrato_atual else "Nenhuma transação registrada")
    print()
    print()
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("-=" * 20)


def cadastrar_endereço():
    endereco['logradouro'] = (str(input("Qual o nome da sua rua: ")))
    endereco['rua'] = (int(input("N. Rua: ")))
    endereco['bairro'] = (str(input("Bairro: ")))
    endereco['uf'] = (str(input("UF: ")))
    cliente['endereço'] = endereco.copy()
    usuario.append(cliente.copy())
    endereco.clear()
    cliente.clear()


def criar_usuario():
    cliente['nome'] = str(input("Qual o seu nome: "))
    cliente['sobreNome'] = str(input("Qual o seu sobrenome: "))
    cliente['dataNasc'] = str(
        input("Qual sua data de nascimento (DD/MM/AAAA): "))
    cliente['CPF'] = int(
        input("Qual o seu CPF (apenas numeros): ").replace('.', '',).replace('-', ''))
    if cliente['CPF'] > 11:
        for cpf in usuario:
            if cpf['CPF'] == cliente['CPF']:
                print("CPF ja existente operação cancelada")
                return
        cadastrar_endereço()
    else:
        print("CPF invalido")


def criar_conta_corrente():
    global numeros_contas_usuario
    if len(usuario) > 0:
        criando_conta_corrente['agencia'] = "0001"
        criando_conta_corrente['numeros da conta'] = numeros_contas_usuario + 1
        criando_conta_corrente['usuario'] = int(
            input("Digite o CPF do usuario: "))
        for cpf in usuario:
            if cpf['CPF'] == criando_conta_corrente['usuario']:
                numeros_contas_usuario += 1
                conta_corrente.append(criando_conta_corrente.copy())
                criando_conta_corrente.clear()
                print("Conta criada!")
                break
        else:
            print("Esse CPF não esta cadastrado em nosso sistema!")
            criando_conta_corrente.clear()
    else:
        print("Não existe Um usuario cadastrado")


def menu():
    print("\n" + "-=" * 30)
    print(" " * 20 + "MENU PRINCIPAL")
    print("-=" * 30)
    print("1 - Criar Usuário")
    print("2 - Criar Conta Corrente")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Mostrar Extrato")
    print("0 - Sair do Sistema")
    print("-=" * 30)


while True:
    menu()
    escolha = int(input("Opção: "))

    if escolha == 1:  # Criar Usuário
        criar_usuario()

    elif escolha == 2:  # Criar Conta Corrente
        criar_conta_corrente()

    elif escolha == 3:  # Depositar
        valor = int(input("Qual o valor deseja depositar: "))
        saldo, transacao_realizados = depositar(
            valor, saldo, transacao_realizados)

    elif escolha == 4:  # Sacar
        if saldo > 0:
            if saque_max > 0:
                print(
                    f"Você tem um limite de 3 saques diários. Restam {saque_max} hoje.")

                valor = int(input("Qual o valor que deseja sacar: "))

                if valor > saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif valor < 0:
                    print("Operação falhou! O valor informado é inválido.")
                elif valor <= 500:
                    saldo, transacao_realizados, transacao_diaria, saque_max = sacar(
                        saldo=saldo, valor=valor, numero_saques=transacao_diaria, limite_saques=saque_max, extrato=transacao_realizados)
                else:
                    print(
                        "Valor de saque ultrapassou o limite de R$500. Tente um valor menor.")
            else:
                print("Limite de saques diário atingido. Tente novamente amanhã.")
        else:
            print("Você não tem saldo em sua conta.")

    elif escolha == 5:  # Mostrar Extrato
        extrato(saldo, extrato_atual=transacao_realizados)

    elif escolha == 0:  # Sair
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
