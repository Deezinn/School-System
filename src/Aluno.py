from Pessoa import *

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self._nota = None  

    @property
    def mostrar_nota(self):
        return self._nota 
    
    @mostrar_nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10: 
            self._nota = valor
        else:
            print("Nota inválida. A nota deve ser entre 0 e 10.")
