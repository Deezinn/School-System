from Aluno import *  

class Turma(Aluno):
    def __init__(self, nome=None, idade=None, email=None, cpf=None):
        super().__init__(nome, idade, email, cpf)
        self.alunos = {}

    def mostrar_aluno(self):
        if len(self.alunos) > 0:
            for chave, aluno in self.alunos.items():
                print(f"ID: {chave}, Nome: {aluno.nome}, Idade: {aluno.idade}, Email: {aluno.email}, CPF: {aluno.cpf}")
        else:
            print("Nenhum aluno cadastrado na turma.")

    def adicionar_aluno(self):
        nome = input("Digite o nome do aluno para adicionar: ")
        idade = input("Digite a idade do aluno: ")
        email = input("Digite o email do aluno: ")
        cpf = input("Digite o CPF do aluno: ")

        aluno = Aluno(nome, idade, email, cpf)
        index = len(self.alunos) + 1
        self.alunos[index] = aluno
        print(f"Aluno {aluno.nome} adicionado com sucesso!")
    

    def modificar_aluno(self):
        try:
            index = int(input("Digite o ID do aluno que deseja modificar: "))
            if index in self.alunos:
                nome = input("Digite o novo nome do aluno: ")
                idade = input("Digite a nova idade do aluno: ")
                email = input("Digite o novo email do aluno: ")
                cpf = input("Digite o novo CPF do aluno: ")
                
                aluno = self.alunos[index]
                aluno.nome = nome
                aluno.idade = idade
                aluno.email = email
                aluno.cpf = cpf

                print(f"Aluno {aluno.nome} modificado com sucesso!")
            else:
                print("Aluno não encontrado.")
        except ValueError:
            print("ID inválido. Por favor, insira um número válido.")

    def remover_aluno(self):
        try:
            index = int(input("Digite o ID do aluno que deseja remover: "))
            if index in self.alunos:
                removed = self.alunos.pop(index)
                print(f"Aluno {removed.nome} removido com sucesso!")
            else:
                print("Aluno não encontrado.")
        except ValueError:
            print("ID inválido. Por favor, insira um número válido.")
