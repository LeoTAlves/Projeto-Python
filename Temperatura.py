temperatura=int(input("Digite a temperatura atual"))

if temperatura <= 15:
    print("Está frio, ligar o aquecedor.")

elif temperatura > 15 and temperatura < 25:
    print("Agradável")

else:
    print("Está calor, ligar o ar condicionado.")
