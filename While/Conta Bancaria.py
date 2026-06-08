def exibir_menu():
    print("\n===================")
    print("Minha Conta")
    print("0 - Sair.")
    print("1 - Depositar.")
    print("2 - Sacar.")
    print("3 - Saldo.")
    print("=====================")

def depositar_valor():

saldo = 0.0

while True:
    exibir_menu()
    opcao = input("Escolha uma opação: ")
