from datetime import datetime


class Transacao:
    def __init__(self):
        self.data_hora = datetime.now()

    def registrar(self, conta: 'Conta'):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        super().__init__()

    def registrar(self, conta: 'Conta'):
        return conta.sacar(self._valor)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        super().__init__()

    def registrar(self, conta: 'Conta'):
        return conta.depositar(self._valor)


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

    def exibir(self):
        if not self._transacoes:
            print("Não existe transaçoes realizadas")
        else:
            print("Extrato de transações")
            for movimentacao in self._transacoes:
                tipo = movimentacao.__class__.__name__
                valor = movimentacao._valor
                data = movimentacao.data_hora.strftime('%d/%m/%Y %H:%M:%S')
                print(f"- {data} | {tipo}: R$ {valor:.2f}")


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta: 'Conta', transacao: Transacao):
        if transacao.registrar(conta):
            conta._historico.adicionar_transacao(transacao)

    def adicionar_conta(self, conta: 'Conta'):
        self._contas.append(conta)
        pass


class Conta():
    def __init__(self, saldo, numero, agencia, cliente: Cliente, historico: Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo

    def nova_conta(self, cliente: Cliente, numero: int):
        pass

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo Insuficiente!!!")
            return False
        self._saldo -= valor
        print(f"Saque de R${valor:.2f} realizado.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor invalido inserido!!!")
            return False
        self._saldo += valor
        print(f"Depósito de R${valor:.2f} realizado.")
        return True

    @property
    def extrato(self):
        return self._historico


class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


class Conta_Corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_hoje = 0
        self._data_ultimo_saque = datetime.now().date()

    def sacar(self, valor):
        hoje = datetime.now().date()
        if hoje != self._data_ultimo_saque:
            self._saques_hoje = 0
            self._data_ultimo_saque = hoje

        if self._saques_hoje >= self._limite_saques:
            print("Limite de saques diários atingido.")
            return False

        if valor > self._limite:
            print(f"Valor máximo de saque é R${self._limite:.2f}.")
            return False

        if valor > self._saldo:
            print("Saldo insuficiente!")
            return False

        self._saldo -= valor
        self._saques_hoje += 1
        print(f"Saque de R${valor:.2f} realizado.")
        return True


def menu():
    print("\n--- MENU BANCO ---")
    print("1 - Criar cliente")
    print("2 - Criar conta corrente")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Ver Extrato")
    print("6 - Sair")


clientes = []
contas = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = str(input("Nome: "))
        cpf = int(input("CPF: "))
        data_nasc = input("Data de nascimento [DD/MM/AAAA]: ")
        endereco = input("Endereço: ")
        cliente = Pessoa_Fisica(endereco, cpf, nome, data_nasc)
        clientes.append(cliente)
        print("Cliente criado com sucesso.")

    elif opcao == "2":
        if not clientes:
            print("Nenhum cliente cadastrado.")
            continue
        for i, c in enumerate(clientes):
            print(f"{i} - {c._nome}")
        indice = int(input("Escolha o cliente para vincular a conta: "))
        cliente = clientes[indice]
        numero = int(input("Número da conta: "))
        conta = Conta_Corrente(0, numero, "0001", cliente, Historico(), 500, 3)
        cliente.adicionar_conta(conta)
        contas.append(conta)
        print("Conta criada com sucesso.")

    elif opcao == "3":
        if not contas:
            print("Nenhuma conta encontrada.")
            continue
        valor = float(input("Valor do depósito: "))
        for i, conta in enumerate(contas):
            print(f"{i} - Conta: {conta._numero} | Cliente: {conta._cliente._nome}")
        indece = int(input("Escolha a conta: "))
        conta = contas[indece]
        cliente = conta._cliente
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)

    elif opcao == "4":
        if not contas:
            print("Nenhuma conta encontrada.")
            continue
        valor = float(input("Valor do saque: "))
        for i, conta in enumerate(contas):
            print(f"{i} - Conta: {conta._numero} | Cliente: {conta._cliente._nome}")
        indice = int(input("Escolha a conta: "))
        conta = contas[indice]
        cliente = conta._cliente
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)

    elif opcao == "5":
        if not contas:
            print("Nenhuma conta encontrada.")
            continue
        for i, conta in enumerate(contas):
            print(f"{i} - Conta: {conta._numero} | Cliente: {conta._cliente._nome}")
        indice = int(input("Escolha a conta: "))
        conta = contas[indice]
        cliente = conta._cliente
        conta.extrato.exibir()
        print()
        print()
        print(f"Saldo atual: R${conta.saldo:.2f}")

    elif opcao == "6":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
