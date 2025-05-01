
# 🏦 Sistema Bancário em Python (Procedural)

Este é um projeto simples de **Sistema Bancário** desenvolvido em **Python**, utilizando uma abordagem **procedural**, com foco em aprendizado de programação, boas práticas, controle de fluxo e estrutura de dados.

## 💻 Funcionalidades

O sistema permite:

- ✅ Criar usuários com dados pessoais e endereço
- ✅ Criar contas bancárias associadas a usuários existentes
- ✅ Realizar depósitos
- ✅ Realizar saques com limites diários
- ✅ Consultar extrato de transações
- ✅ Sistema de limite de transações por dia

## 🛠️ Tecnologias Utilizadas

- Linguagem: [Python 3.x](https://www.python.org/)
- Módulos: `datetime` (nativo)

## 📂 Estrutura do Código

- `usuario`: lista que armazena todos os usuários
- `cliente`, `endereco`: dicionários temporários para cadastro
- `conta_corrente`: lista com todas as contas bancárias criadas
- `depositar(valor, saldo, extrato)`: função para depósito
- `sacar(saldo, valor, extrato, numero_saques, limite_saques)`: função para saque
- `extrato(saldo, extrato_atual)`: exibe extrato da conta
- `criar_usuario()`: coleta e armazena dados de um novo usuário
- `criar_conta_corrente()`: vincula uma conta a um CPF válido
- `menu()`: exibe opções do sistema

## 🧪 Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/Renanito69/Sistema-Bancario-com-python.git
```

2. Navegue até a pasta do projeto e execute o arquivo Python:

```bash
cd Sistema-Bancario-com-python
python sistema_bancario.py
```

3. Siga o menu no terminal para interagir com o sistema.

## 📌 Regras de Negócio

- Cada usuário pode ter **uma ou mais contas correntes**
- Cada CPF deve ser **único**
- Limite de **3 saques diários**, com valor máximo de R$500 por saque
- Limite de **10 transações** (depósitos ou saques) por dia
- O extrato é exibido com data e hora de cada operação

## 🚀 Melhorias Futuras

- 💳 Integração com interface gráfica (Tkinter ou PyQt)
- 🔐 Implementar autenticação com senha
- 🧾 Armazenamento de dados em arquivos ou banco de dados
- 🧱 Versão com Programação Orientada a Objetos

## 👨‍💻 Autor

**Renan Cristian**  
Estudante de Análise e Desenvolvimento de Sistemas (3º semestre)  
Curso: Introdução à Programação - Recode / Imersão Front-End - Alura / Python - Dio.me 
GitHub: [github.com/Renanito69](https://github.com/Renanito69)

---

📬 Para dúvidas ou sugestões, fique à vontade para abrir uma *issue* ou contribuir com o projeto!
