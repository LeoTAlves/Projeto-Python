usuario_correto = "admin"
senha_correta = "1234"

usuario = ""
senha = ""

while usuario != usuario_correto or senha != senha_correta:
    usuario = input("Digite o nome usuario: ")
    senha = input("Digite a senha: ")

    if usuario != usuario_correto or senha != senha_correta:
        print("Usuario ou senha invalidos. Tente novamente")
    else:
        print("Acesso permitido")