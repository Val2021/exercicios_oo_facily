"""
Crie uma classe para representar datas com as seguintes regras: 
a. deve ter três atributos: o dia, o mês e o ano; 
b. deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos; c. encapsule cada um dos atributos; 

"""

class Data:
    def __init__(self,dia,mes,ano) -> None:
        self._dia = dia
        self.valida_dia()
        self._mes = mes
        self.valida_mes()
        self._ano = ano
        self.valida_ano()

    @property
    def dia(self):
        return self._dia
    
    @property
    def mes(self):
        return self._mes
    
    @property
    def ano(self):
        return self._ano
    
    def valida_dia(self):
        if self._dia > 31:
            raise Exception("Dia invalido! Digite um dia entre 1 e 31")
    
    def valida_mes(self):
        if self._mes > 12:
            raise Exception("Mes invalido! Digite um mes entre 1 e 12")
    
    def valida_ano(self):
        if self._ano <= 0:
            raise Exception("Ano invalido! Digite um ano maior que 0 ")
    
        
   
            
app = Data(4,14,2021)
          
        