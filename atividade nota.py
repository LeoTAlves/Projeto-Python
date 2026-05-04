import math

nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))

nota = (nota1 + nota2 + nota3)/3
nota = round(nota)
# Outra forma de arrendondamento para cima é utilizando o "math.ceil (apenas um casa)"
# Outra forma de arrendondamento para baixo é utilizando o "math.floor (apenas um casa)"

if nota >= 0 and nota <= 5:
    print("Não Aprovado " , nota)

elif nota > 5 and nota <= 7:
    print("Recuperação " , nota)

elif nota > 7 and nota <= 10:
    print("Aprovado " , nota)

else:
    print ("Número não condiz com uma nota de 0 a 10")