from Turma import *

class Menu:
    def __init__(self) -> None:
        self.turma = Turma()
       
    def executarMenu(self):
        while True:
            print("\n1. Adicionar Aluno")
            print("2. Mostrar Alunos")
            print("3. Adicionar Nota")
            print("4. Remover Aluno")
            print("5. Sair")

                
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.turma.adicionar_aluno()
            elif opcao == "2":
                alunos = self.turma.mostrar_alunos()
                if alunos:
                    for aluno in alunos:
                        print(aluno)
                else:
                    print("Não há alunos na turma.")
            elif opcao == "3":
                self.turma.adicionar_nota()
            elif opcao == "4":
                self.turma.remover_aluno()
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")
        