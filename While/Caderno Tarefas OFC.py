def exibir_menu():
    print("\n===================")
    print("Menu")
    print("1 - Adcionar tarefas.")
    print("2 - Listar tarefas.")
    print("3 - Remove tarefas.")
    print("0 - Sair.")
    print("=====================")

def adcionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para exibir. ")
    else:
        for posicao_tarefa, tarefa in enumerate(tarefas, start =1):
            print(f"{posicao_tarefa} - {tarefa}")

def remover_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para remover. ")
    else:
        tarefa = int(input("Digite o numero da tarefa que deseja remover"))
        if tarefa > 0 and tarefa <= len(tarefas):
            # tarefa = tarefa - 1
            tarefa_removida = tarefas.pop(tarefa)
            print(f"Tarefa removida: {tarefa_removida}")
        else:
            print(f"Tarefa não existe. Digite uma opção valida!")

tarefas = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opação: ")

    if opcao == "0":
        print("Encerrando o programa")
        break
    elif opcao == "1":
        adcionar_tarefa(tarefas)
    elif opcao == "2":
            listar_tarefa(tarefas)
    elif opcao == "3":
        remover_tarefa(tarefas)
    else:
        print("Opção invalida!")
    