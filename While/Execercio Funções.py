def somar(n1 , n2):
    total = n1 + n2
    print(f" {n1} + {n2} = {total}")
    
def subtrair(n1 , n2):
    total = n1 - n2
    print(f" {n1} - {n2} = {total}")
    
def multiplicar(n1 , n2):
    total = n1 * n2
    print(f" {n1} * {n2} = {total}")
    
def dividir(n1 , n2):
    if n2 == 0:print(" Não tem como dividir por ZERO")
    else: print(f" {n1} / {n2} = {round(n1 / n2, 2)}")
    

while True:
    menu = """
    === CALCULADORA ===
    
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (x)
    4 - Divisão (/)
    0 - Sair
    """
    print(menu)

    escolha = input("digite a opção: ")

    if escolha == "0" : break

    if escolha not in ["1", "2", "3", "4", "0"]:
        print("Opção invalida! Tente novamente")
        continue

    n1 = int(input("digite um número: "))
    n2 = int(input("digite outro número: "))
    
    if escolha == "1": somar (n1 , n2)    
    elif escolha == "2": subtrair (n1 , n2)    
    elif escolha == "3": multiplicar (n1 , n2)    
    elif escolha == "4": dividir (n1, n2)
    else:print("opção invalida")
    

