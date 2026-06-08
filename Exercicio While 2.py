numero = 0
palpite = -1
erro = -1
while palpite != numero:
    palpite = int(input("Digite um número aleatorio: "))
    erro = erro + 1
if erro <= 1:
    print(f"Você teve {erro} erro. ")
else:
    print(f"Você teve {erro} erros. ")