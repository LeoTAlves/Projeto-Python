frutas = ["manga", "banana" , "abacaxi" , "laranja" , "amora"]

fruta_favorita = input("Qual a sua fruta favorita?:")

#Se a fruta favorita NÃO ESTÁ NA lista frutas
if fruta_favorita not in frutas:
    #Faça isso (exibir mensagem e sai do sistema):
    print("Sua fruta favorita nao está na lista!")
    print("Adicionando ...")
    frutas.append(fruta_favorita)

#Para cadaa posição (indice) e fruta na lista numerada da fruta
for posicao, fruta in enumerate(frutas):
    #Faça isso:
    #Se a fruta dessa interação é igual a fruta favorita
    if fruta == fruta_favorita:
        #Salva numa nova variavel a posição dessa interação
        posicao_fruta_favorita = posicao
        #Quebra o for (faz ele parar)
        break

#Saida do algoritimo (print)
print(f"Minha fruta favorita está na posição índice {posicao_fruta_favorita}")