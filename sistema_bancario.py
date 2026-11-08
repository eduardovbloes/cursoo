sistema_online = True
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

print("---Bem vindo ao sistema bancario---\n")
menu = """
O que deseja fazer?
[1]Deposito
[2]saque
[3]extrato
[4]sair
>=  """
while sistema_online == True:
    opcao = input(menu)
    
    if opcao == "1":
        print("deposito")
        valor = float(input("Insira o valor do deposito: R$"))
        if valor > 0:
            print("deposito concluido")
            saldo += valor
            extrato += f"Valor: R$ {valor:.2f}\n"
        else:
            print("digite um numero valido")
        
    elif opcao == "2":
        print("saque")
        valor = float(input("Insira o valor do saque: R$"))
        if valor > saldo:
            print("Transacao negada por falta de saldo")
            continue
        elif valor > limite:
            print("operacao negada!! \nSeu limite de saque é de R$500")
            continue
        elif numero_saques >= limite_saques:
            print("Voce atingiu seu limite de saques diarios")
            continue
        else:
            print("saque realizado com sucesso")
        saldo -= valor
        extrato += f"Valor: R$ {valor:.2f}\n"
        numero_saques += 1
        
    elif opcao == "3":
        print("====== extrato ======")
        print("nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}\n")
        
    elif opcao == "4":
        print("obrigado volte sempre!!!")
        sistema_online = False
        
    else:
        print("opcao invalida escolha novamente")