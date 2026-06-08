def adicionar_tarefa(tarefas):
    texto = input("Digite a tarefa: ")
    tarefas.append(texto)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")


def remover_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para remover.")
        return

    listar_tarefas(tarefas)

    try:
        posicao = int(input("Digite o número da tarefa a remover: "))
        tarefas.pop(posicao - 1)  # usuário vê a partir de 1
        print("Tarefa removida com sucesso!")
    except (ValueError, IndexError):
        print("Posição inválida.")


# Lista vazia criada antes do while
tarefas = []

while True:
    print("\n=== CADERNO DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(tarefas)

    elif opcao == "2":
        listar_tarefas(tarefas)

    elif opcao == "3":
        remover_tarefa(tarefas)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")