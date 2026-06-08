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
    
    if escolha == "1":
        total = n1 + n2
        print(f" {n1} + {n2} = {total}")
    
    elif escolha == "2":
        total = n1 - n2
        print(f" {n1} - {n2} = {total}")
    
    elif escolha == "3":
        total = n1 * n2
        print(f" {n1} * {n2} = {total}")
    
    elif escolha == "4":
        if n2 == 0: print(" Não tem como dividir por ZERO, BURRO ")

        else:
            total = n1 / n2
            print(f" {n1} / {n2} = {total}")
        
    else:
        print("opção invalida")
    
