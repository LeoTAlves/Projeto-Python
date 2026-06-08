def exibir_menu():
    print("\n====================")
    print("CONTA BANCÁRIA")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Saldo")
    print("0 - Sair")
    print("====================")

def depositar(saldo, valor):
    saldo = saldo + valor
    print("Depósito realizado com sucesso!")
    return saldo

def sacar(saldo, valor):
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - valor
        print("Saque realizado com sucesso!")
    return saldo 

def ver_saldo(saldo):
    print(f"Saldo atual: R$ {saldo:.2f}")

saldo = 0.0

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o programa. Até mais!")
        break
        
    elif opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo = depositar(saldo, valor_deposito)
        
    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        saldo = sacar(saldo, valor_saque)
        
    elif opcao == "3":
        ver_saldo(saldo)
        
    else:
        print("Opção inválida! Tente novamente.")