def menu():
	menu = '''\n
  =======MENU=======
  [1]Depositar
  [2]Sacar
  [3]Extrato
  [4]Novo Cliente
  [5]Nova Conta
  [6]Lista de contas
  [0]Sair
  => '''
	return input(menu)

def depositar(valor, saldo, extrato, /):
	if valor > 0:
		saldo += valor
		extrato += f"\nDepósito no valor de {valor:.2f}"
		print("\nValor depositado com sucesso!")
	else:
		print("\nERRO! Depósito não realizado.")

	return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, numero_saque, limite_saque):
	sem_saldo = valor > saldo
	limite_diario = valor > limite
	tres_operacoes = numero_saque >= limite_saque

	if sem_saldo:
		print("\nSaque não realizado! Você não possui saldo para essa transação.")

	elif limite_diario:
		print("\nSaque não realizado! Você pode sacar até R$500 por operação.")

	elif tres_operacoes:
		print("\nSaque não realizado. Você atingiu seu limite de três saques por dia.\nVolte amanhã.")

	elif valor > 0:
		saldo -= valor
		extrato += f"\nSaque no valor de {valor:.2f}"
		numero_saque += 1
		print("\nSaque efetuado!!\nValor retirado da conta com sucesso!")
	
	else:
		print("\nERRO! Saque não realizado. Valor inválido.")
	
	return saldo, extrato

def extrato_da_conta(saldo, /, *, extrato):
	print("\n==========EXTRATO==========")
	print("Nenhuma movimentação realizada." if not extrato else extrato)
	print(f"\nSaldo da conta: R$ {saldo:.2f}")
	print("===========================")

def novo_cliente(clientes):
	cpf = input("Informe o CPF (somente números): ")
	cliente = tem_cliente(cpf, clientes)

	if cliente:
		print("\nJá existe um cliente cadastrado com esse CPF!")
		return
	
	nome = input("Digite o nome completo: ")
	data_nascimento = ("Digite a data de nascimento (dd-mm-aaaa): ")
	endereco = input("Digite o endereço (logradouro, num - bairro - cidade/sigla estado): ")

	clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

	print("\nNovo cliente cadastrado com sucesso!")

def tem_cliente(cpf, clientes):
	filtro_clientes = [cliente for cliente in clientes if cliente["cpf"] == cpf]
	return filtro_clientes[0] if filtro_clientes else None

def nova_conta(agencia, numero_conta, clientes):
	cpf = input("Digite o CPF do cliente: ")
	cliente = tem_cliente(cpf, clientes)

	if cliente:
		print("Nova conta criada com sucesso!")
		return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
	
	print("Usuário não encontrado!!!")
	return None

def listagem(contas):
	for conta in contas:
		info = f"""
	Agencia: {conta["agencia"]}
	C/C: {conta["numero_conta"]}
	Titular: {conta["cliente"]["nome"]}
	"""
		print("-" * 40)
		print(info)

def sistema_bancario():
	AGENCIA = "0001"
	LIMITE = 500

	saldo = 0
	extrato = ''
	numero_saque = 0
	limite_saque = 3
	clientes = []
	contas = []

	while True:
		opcao = menu()

		if opcao == "1":
			valor = float(input("Qual o valor do depósito? R$"))
			saldo, extrato = depositar(valor, saldo, extrato)
			
		elif opcao == "2":
			valor = float(input("Qual o valor do saque? R$"))
			saldo, extrato = sacar(valor=valor, saldo=saldo, extrato=extrato, limite=LIMITE, numero_saque=numero_saque, limite_saque=limite_saque)
			
		elif opcao == "3":
			extrato_da_conta(saldo, extrato=extrato)

		elif opcao == "4":
			novo_cliente(clientes)

		elif opcao == "5":
			numero_conta = len(contas) + 1
			conta = nova_conta(AGENCIA, numero_conta, clientes)

			if conta:
				contas.append(conta)
		
		elif opcao == "6":
			listagem(contas)

		elif opcao == "0":
			print("Saindo...\nObrigado por usar nosso banco!")
			break

		else:
			print("Erro! Selecione novamente a opção desejada.")

sistema_bancario()