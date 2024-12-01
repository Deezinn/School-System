class Pessoa:
    def __init__(self, nome):
        if not nome or not nome.strip():
            raise ValueError("O nome não pode ser vazio ou nulo.")
        self.__nome = nome.strip().title()