from Turma import *

class Main:
    def __init__(self):
        pass  
    
    def escolha(self):
        print('Digite [1] para mostrar todos os alunos.')       
        print('Digite [2] para adicionar aluno.') 
        print('Digite [3] para modificar algum dado do aluno.')
        print('Digite [4] para deletar algum aluno.')        
        return input("Escolha uma opção: ")
    
    def execute(self):
        turma = Turma()
        while True:
            valor = self.escolha() 
            match valor:
                case '1':
                    turma.mostrar_aluno()
                case '2':
                    turma.adicionar_aluno()
                case '3':
                    turma.modificar_aluno()
                case '4':
                    turma.remover_aluno()
                case _:
                    print("Opção inválida.")
            
            continuar = input("Deseja continuar? (s/n): ").strip().lower()
            if continuar != 's':
                print("Encerrando o programa.")
                break

if __name__ == "__main__":
    main = Main()
    main.execute()
