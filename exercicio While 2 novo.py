contador = 0
numeros = []
numero = -1
while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
    if numero != 0:
        contador = contador + 1
        numero.append(numeros)
print(f"Quantidade de números digitados: {contador}")