from Pessoa import *

class Aluno(Pessoa):
    def __init__(self,nome,idade,email,cpf,nota):
        super().__init__(nome,idade,cpf)
        self.email= email
        self.nota = nota
