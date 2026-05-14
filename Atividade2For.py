produtos = ["camiseta", "calça", "par meias", "boné", "par luvas"]
preços = [40.00, 80.00, 15.00, 20.00, 20.00]
quantidades = [2, 4, 2, 3, 2]
total = []

# ANTES, FARIA ASSIM PARA PEGAR O PRODUTO E PREÇO:

print(f"O produto {produtos[0]} custa R$ {preços[0]}")

for indice, produto in enumerate(produtos):
    preço = preços[indice] # preço = preços[0]
    quantidade = quantidades[indice]
    subtotal = preço * quantidade
    total.append(subtotal)

    mensagem = f"""
    -------------------------------------------------
    Produto:     {produto}
    Quantidade:  {quantidade}
    Valor Unit.: {preço}
    Sub. total:  {subtotal}
    -------------------------------------------------

    """
    print(mensagem)

print(f"O valor total da compra deu: R${sum(total)}")