"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
do mês por extenso.
Ex: Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973.
"""



class DataNascimento:

    def __init__(self) -> None:
        self.data = ""
        self.month = ""
        self.day = ""
        self.year = ""
        
    def get_data(self):
        data = input("Digite a sua data de nascimento no formato  (dd/mm/aaaa) {} " .format(self.data))
        self.day = int(data.split("/")[0])
        self.year = int(data.split("/")[2])
        self.data = int(data.split("/")[1])
        return self.data , self.day,self.year 
        
    def get_mounth(self):
        list_month = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self.month = list_month[self.data - 1]
        return self.month
    
    
    def show_data(self):
        print("Você nasceu em  {}  de {}  de {} " .format(self.day, self.month, self.year))


aniversario = DataNascimento()
aniversario.get_data()
aniversario.get_mounth()
aniversario.show_data()