produtos = ["Arroz", "Feijão", "Ovos"]
precos = [5.99, 6.9, 12.99]

for posicao, produto in enumerate(produtos):
    if precos[posicao] < 10.00:
        preco_ajustado = round(precos[posicao] * 1.10, 2)
        print(f"Produto: {produto} custava R$ {precos[posicao]}, agora custa R$ {preco_ajustado} ")
    else:
        print(f"Produto: {produto} custava R$ {precos[posicao]}")
    