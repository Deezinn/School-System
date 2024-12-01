from Aluno import *

class Turma():
    def __init__(self):
        self.alunos = {}
        
    def mostrar_alunos(self):
        return self.alunos
    
    def adicionar_aluno(self):
        aluno_nome = input("Digite o nome do aluno: ").strip()
        if not aluno_nome or len(aluno_nome) <= 2:
            print('Insira um nome válido')
            return
        aluno = Aluno(aluno_nome)
        self.alunos[aluno_nome] = aluno
        print(f"Aluno {aluno_nome} adicionado com sucesso!")
    
    def modificar_aluno(self):
        aluno_nome_modificar = input("Digite o nome do aluno que deseja modificar: ").strip()
        if aluno_nome_modificar not in self.alunos:
            print("Aluno não encontrado, tente novamente.")
            return
        novo_nome = input("Digite o novo nome do aluno: ").strip()
        aluno = self.alunos.pop(aluno_nome_modificar)
        aluno.nome = novo_nome
        self.alunos[novo_nome] = aluno
        print(f"Nome do aluno modificado para {novo_nome}.")
    
    def remover_aluno(self):
        aluno_nome_deletar = input("Digite o nome do aluno para ser deletado: ").strip()
        if aluno_nome_deletar not in self.alunos:
            print("Aluno não encontrado.")
        else:
            self.alunos.pop(aluno_nome_deletar)
            print(f"Aluno {aluno_nome_deletar} removido com sucesso!")
    
    def adicionar_nota(self):
        nomeAluno = input("Qual aluno deseja adicionar nota? ").strip()
        if nomeAluno not in self.alunos:
            print('Aluno não encontrado.')
            return

        try:
            nota = float(input("Digite a nota do aluno (0 a 10): "))
            if 0 <= nota <= 10:
                aluno = self.alunos[nomeAluno]
                aluno.nota = nota
                print(f"Nota de {nomeAluno} atribuída com sucesso!")
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um valor numérico válido para a nota.")

