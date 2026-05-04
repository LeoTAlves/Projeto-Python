valor=int(input("Digitar o valor do pedido: "))

if valor >= 100:
    total= valor * 0.90
    print("o valor total foi de: ", total)

else:
    total= valor
    print("O valor total foi de: ", total)