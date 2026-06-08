nome_correto = "admin"
senha_correta = "1234"

nome_usuario = input("Digite o nome usuario: ")
senha = input("Digite a senha: ")

if nome_usuario == nome_correto and senha == senha_correta:
    print("Acesso Permitido")
else:
    print("Acesso Negado")