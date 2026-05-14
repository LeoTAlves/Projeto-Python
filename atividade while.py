import random
numero_secreto = random.randint (1, 10)
palpite = 0
tentativa = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe um número (1 a 10): "))
    if palpite != numero_secreto:
        print("Errou imbecil, tente novamente.")

    tentativa = tentativa + 1

if tentativa <= 1:
    print(f"ACERTOUUUU, O miserável e um genio. Você precisou de {tentativa} tentativa. ")
else:
    print(f"ACERTOUUUU, O miserável e um genio. Você precisou de {tentativa} tentativas. ")