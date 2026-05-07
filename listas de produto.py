produto=["arroz", "feijão", "macarrão", "leite", "pão"]
preços=[20.00 , 8.00 , 2.00 , 4.50 , 8.00]

print("lista completa,", produto)

print("primeiro produto,", produto[0])

print("último produto,", produto[4])

print("total produtos na lista,", len(produto))

#Para exibir:
print(f"O produto {produto[0]} custa R$ {preços[0]}")

#Para remover o ultimo produto e o preço também:
produto.remove(produto[-1])
preços.remove(preços[-1])

#Para somar o preço de todos os produtos:
total=sum(preços)
print(f"O total deu R${total}")

# Logica condicional if/else para descontos:
if total <30:
    exit()
else:
    desconto = 0.95
    total = total * desconto
    print(f"O total com desconto é de R$:{total}.")