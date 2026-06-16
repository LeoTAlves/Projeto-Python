class Produto:
    def __init__(self, nome: str, preco: float, setor: str):
        self.nome = nome
        self.preco = preco
        self.seotr = setor

    def carrinho(self):
        print(f"Nome: {self.nome}")
        if not self.preco:
            print("Não possui itens no carrinho.")
            return
        
        for ordem_preco, preco in enumerate(self.preco, start=1):
            print(f"O valor do item {ordem_preco}: {preco}")

def exibir_menu():
    print("\n====================")
    print("1 - Cadastrar produtos")
    print("2 - Calcular total")
    print("3 - Filtrar por setor")
    print("0 - Sair")
    print("====================")

#Opção 1
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    setor = input("Digite o setor do produto: ")
    produto = Produto (nome, preco, setor)
    carrinho.append(produto)

# Opção 2
def exibir_produtos_e_total():
    if not carrinho:
        print("Não há produto cadastrado")
        print("Total do carrinho: R$0.0")
        return
    
    total = 0 
    for produto in carrinho:
        produto.exibir()
        total += produto.preco
    print(f"total do carrinho: R${total}")

#Opção 3
def filtrar_por_setor():
    setor = input("Digite o setor para filtrar: ")
    encontrou = False
    for codigo_produto, produto in enumerate(carrinho, start-1):
        if setor == produt.setor:
            print(f"codigo produto: {codigo_produto}")
            produto.exibir()
            encontrou = True
    if not encontrou:
        print(f"Nenhum produto do setor digitado ({setor}) foi encontrado no carrinho")
    
carrinho = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        exibir_produtos_e_total()
    elif opcao == "3":   
        filtrar_por_setor()  
    else:
        print("Opção Inválida")