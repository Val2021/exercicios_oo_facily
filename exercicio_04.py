"""
Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0
"""



class Aluno:

    def __init__(self,nota1,nota2) -> None:
        self.notas = [nota1,nota2]
    
    def calc_media(self) -> float:
        resultado = sum(self.notas)
        return resultado / (len(self.notas))

class Controller:
    
    def __init__(self,alunos) -> None:
        self.alunos = alunos
    
    def cal_media_aluno(self):
        self.list_media = []
        for i in self.alunos:
            self.list_media.append(i.calc_media()) #lazy evaluation
    
    def over_seven(self):
        over_sete = []
        for i in self.list_media:
            if i >= 7:
                over_sete.append(i)
        return over_sete


    
class Facade:

    def create_alunos(self):
        i = 0
        list_aluno =[]
        while i < 5:
            nota1 = float(input("Digite a nota 1 do aluno {}:  " .format(i+1)))
            nota2 = float(input("Digite a nota 2 do aluno {}:  " .format(i+1)))
            
            list_aluno.append(Aluno(nota1,nota2))

            i += 1
        
    
        self._controler = Controller(list_aluno)
    
    def show_qtd(self):
        self._controler.cal_media_aluno()
        show_qtd = self._controler.over_seven()
        print("O número de alunos com média maior ou igual a 7.0 é {}" .format(len(show_qtd)))


api = Facade ()
api.create_alunos()
api.show_qtd()

        

        


        

   