"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
do mês por extenso.
Ex: Data de Nascimento: 29/10/1973
Você nasceu em 29 de Outubro de 1973.
"""



class DateBirthday:

    def __init__(self) -> None:
        self.month = ""
        self.day = ""
        self.year = ""
        
    
    def get_birthdate(self,data):
        self.day = int(data.split("/")[0])
        self.month = int(data.split("/")[1])
        self.year = int(data.split("/")[2])
        return self.day,self.month,self.year
        
        
    def get_month_data(self):
        list_month = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self.month = list_month[self.month - 1]
        return self.month
    
    
    def show_date(self):
        print("Você nasceu em  {}  de {}  de {} " .format(self.day,self.month, self.year))

if __name__ == "__main__":
    data = input("Digite a sua data de nascimento no formato  (dd/mm/aaaa) : " )
    aniversario = DateBirthday()
    aniversario.get_birthdate(data)
    aniversario.get_month_data()
    aniversario.show_date()