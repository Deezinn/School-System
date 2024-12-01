from Menu import *

class Main:
    def __init__(self):
        self.menu = Menu() 
    
    def Executar_tudo(self):
        self.menu.executarMenu()
    
if __name__ == "__main__":
    main = Main()  
    main.Executar_tudo()  
