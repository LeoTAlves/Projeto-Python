def exibir_menu():
    print("\n====================")
    print("CONTA BANCÁRIA")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Saldo")
    print("0 - Sair")
    print("====================")

def depositar(saldo):
    valor = float(input("Digite um valor para deposito: "))
    saldo = saldo + valor
    print(f"Depósito de {valor} realizado com sucesso!")
    return saldo

def sacar(saldo):
    saque = float(input("Digite um valor para saque: "))
    if saque > saldo:
        print("Saldo insuficiente!")
        return saldo
    
    saldo = saldo - saque
    print(f"Saque de {saque} realizado com sucesso!")
    return saldo 

def ver_saldo(saldo):
    print(f"Saldo atual: R$ {saldo}")

saldo = 0.0
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o programa. Até mais!")
        break
        
    elif opcao == "1":
        saldo = depositar(saldo)
        
    elif opcao == "2":
        saldo = sacar(saldo)
        
    elif opcao == "3":
        ver_saldo(saldo)
        
    else:
        print("Opção inválida! Tente novamente.")