class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def exibir(self):
        print(f"Aluno: {self.nome} | Nota: {self.nota}")

    def situacao(self):
        if self.nota >= 6:
            print("Aluno Aprovado!")
        else:
            print("Aluno Reprovado")
    

def cadastro_aluno():
    print("\nCADASTRANDO ALUNO...")
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    aluno = Aluno(nome, nota)
    alunos.append(aluno)

def exibir_alunos():
    if not alunos:
        print("Não há alunos cadastrado! ")
        return
    
    for aluno in alunos:
        aluno.exibir()

def exibir_situacao()
        


alunos = []

cadastro_aluno()
exibir_alunos()
exibir_situacao()

