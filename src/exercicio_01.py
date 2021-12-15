"""
Faça um Programa que leia 4 notas de alunos e, ao final, mostre na tela as notas lidas e a respectiva média
"""

class Nota:

    def __init__(self, nota:str) -> None:
        self.nota = nota

    def get_nota(self)-> int:
        return self.nota
    
    def set_nota(self,nota)-> None:
        self.nota = nota  

    def __repr__(self) -> int:
        return self.nota

class Aluno:

    def __init__(self,qtd_notas:int) -> None:
        self.qtd_notas = qtd_notas
        self.list_nota = []
    

    def inserir_notas(self, nota):

        nota = Nota(nota)
        self.list_nota.append(nota)
        
    def get_media(self):
        return sum([nota.get_nota() for nota in self.list_nota]) / self.qtd_notas

    
    def __repr__(self) -> str:
        list_nota = ""
        for nota in self.list_nota:
            list_nota += " \n " + str(nota.get_nota())
        return f"As notas lidas são {list_nota} e a média é {str(self.get_media())} "

if __name__ == "__main__":

    aluno = Aluno(4)
    aluno.inserir_notas()
    print(aluno)
        
    
        
       
        




    


