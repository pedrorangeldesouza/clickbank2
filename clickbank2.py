saldo = 0
limite = 500
limite_saque = 3
saques_efetuados = 0
usuarios = []
contas = []
enderecos = []
agencia = '0001'


def deposito():
    global saldo
    valor = float(input("Digite o valor a depositar: R$"))
    
    if valor > 0:
        saldo += valor
        print(f'O depósito de R${valor:.2f} foi efetuado com sucesso.')
    else:
        print('Digite um número válido')


def saque():
    global saldo
    global limite
    global limite_saque
    global saques_efetuados
    valor = float(input("Digite o valor a sacar: R$"))
    
    if valor <= saldo and saques_efetuados < limite_saque and valor <= limite:
        saldo -= valor
        saques_efetuados += 1
        print(f'O saque de R${valor:.2f} foi efetuado com sucesso!')
    elif valor > limite:
        print('limite excedido')
    elif valor > saldo:
        print(f'Você não te saldo o suficiente. O seu saldo é de {saldo:.2f}')
    elif saques_efetuados >= limite_saque:
        print('O limite de 3 saques diários foi excedido. Entre em contato com o seu gerente')
    else:
        print('Digite um número válido!')


def extrato():
    print(f'O Valor do seu saldo atual é de R${saldo:.2f}')


def novo_usuario():
    cpf = int(input("Digite seu CPF (Somente Números): "))
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado")
            return
    
    nome = str(input('Digite seu nome completo: '))
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    telefone = int(input('Digite seu telefone: '))
    endereco = input("Digite o endereço (Rua, Número - Bairro - Cidade/Estado): ")


    usuarios.append({
        'cpf':cpf, 
        'nome':nome, 
        'data_nascimento':data_nascimento, 
        'telefone':telefone, 
        'endereco':endereco
        })

    enderecos.append([endereco])



def abrir_conta():
    cpf = int(input("Digite seu CPF (Somente Números): "))
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            numero_conta = len(contas) + 1
            contas.append({
                'agencia': agencia,
                'numero_conta': numero_conta,
                'cpf': cpf
            })
            print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")
            return
    
    print("CPF não cadastrado. Faça cadastro na aba Novo Usuário")


def listar_contas():
    print(contas)


def sair():
    print('Obrigado por contar conosco para suas transações. Até Logo!!')


while True:
    print("\n----ClickBank----")
    print("\n------Saldo------")
    print(f"--------{saldo:.2f}--------")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Novo Usuário")
    print("[5] Abrir Conta")
    print("[6] Listar Contas")
    print("[7] Sair")

    opcao_escolhida = int(input("Escolha uma das opções acima: ")) 

    if opcao_escolhida == 1:
        deposito()

    elif opcao_escolhida == 2:
        saque()
    
    elif opcao_escolhida == 3:
        extrato()

    elif opcao_escolhida == 4:
        novo_usuario()

    elif opcao_escolhida == 5:
        abrir_conta()

    elif opcao_escolhida == 6:
        listar_contas()

    elif opcao_escolhida == 7:
        sair()
        break
    else:
        print("Opção Inválida")