produtos=["arroz", "feijão", "macarrão", "leite", "pão"]
preços=[20.00 , 8.00 , 2.00 , 4.50 , 8.00]

print("lista completa,", produtos)

print("primeiro produto,", produtos[0])

print("último produto,", produtos[4])

print("total produtos na lista,", len(produtos))

#Para exibir:
print(f"O produto {produtos[0]} custa R$ {preços[0]}")

#Para remover o ultimo produto e o preço também:
produtos.remove(produtos[-1])
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