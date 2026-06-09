class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def exibir(self):
        print(f"Produto: {self.nome} | Preço: {self.preco} | Quantidade: {self.qtd}")

#Segunda forma de fazer
produto_2 = Produto("Feijão", 10.0, 15)

produto_2.exibir()