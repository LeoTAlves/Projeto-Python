valor=int(input("Digitar o valor do pedido: "))

"""

Regra de negócio:
* Se a venda for até 100 reais, nao tem desconto
* Se a venda for entre 100.01 e 299.99 reais, dê 10% de desconto
* Se a venda dor acima de 300 reais, dê 15% de desconto

"""


if valor <= 100:
    print(f"O valor da compra deu R${valor}")
    exit()
    
elif valor > 100 and valor <= 299.99:
    desconto = 0.90

else:
    desconto = 0.85

total = valor * desconto

descontopercentual = (1 - desconto) * 100
descontopercentual = round(descontopercentual)

# print("O valor total foi de: ", total, ". Se desconto foi de: ", descontopercentual, "%")

print(f"Sua compra de R${valor}. Você ganhou {descontopercentual}%" f" de desconto. O total agora é R${total}.")

textoResultado = f"""
Sua compra de R${valor}
Você ganhou {descontopercentual}% de desconto.
O total agora é {total}

"""
print(textoResultado)