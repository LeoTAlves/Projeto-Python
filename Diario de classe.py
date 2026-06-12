class Aluno:
    def __init__(self, nome, notas=[]):
        self.nome = nome
        self.notas = notas

    def exibir(self):
        print(f"Aluno: {self.nome}")
        if self.notas:
            for ordem_nota, nota in enumerate(self.notas,1):
                print(f"Nota nº {ordem_nota}: {nota}")

    def situacao(self):
    
        self.notas

def exibir_menu():
    print("========================")
    print("1 - Cadastrar o Aluno")
    print("2 - Lançar Notas")
    print("3 - Ver Situação")
    print("4 - Listar Alunos")
    print("0 - Sair")
    print("========================")

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)
    alunos.append(aluno)
    print(f" Aluno {nome} cadastrado com sucesso")

def lancar_nota()
    indice = int(input("Digite o codigo do aluno: ")) # 0
    aluno = alunos[indice] 
    nota = float(input("Digite a nota para ser lançado: "))
    aluno.notas.append(nota)
    print(f"Nota {nota} lançada para o aluno {aluno.nome}")