class Pessoa:
    def __init__(self, nome):
        if not nome or not nome.strip():
            raise ValueError("O nome não pode ser vazio ou nulo.")
        self.__nome = nome.strip().title()
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,value):
        self.nome = value
        return self.nome
        