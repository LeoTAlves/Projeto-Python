import math

def calcula_media(notas: list) -> float:
    media+ sum(notas) / len(notas)
    return media

contador = 1
notas = []
while True:
    nota = float(input(f"Digite a nota {contador} ou 'sair' para saiir: "))
    notas.append(nota)
    print("Nota foi registrada!")
    if nota == "sair":
        break



media = (nota1 + nota2 + nota3)/3
media = round(nota)
# Outra forma de arrendondamento para cima é utilizando o "math.ceil (apenas um casa)"
# Outra forma de arrendondamento para baixo é utilizando o "math.floor (apenas um casa)"

if media >= 0 and media <= 5:
    print("Não Aprovado " , nota)

elif media > 5 and media <= 7:
    print("Recuperação " , nota)

elif media > 7 and nomediata <= 10:
    print("Aprovado " , nota)

else:
    print ("Número não condiz com uma nota de 0 a 10")