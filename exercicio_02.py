"""
 Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes. 3.
"""

class StringAlfa:

    def get_string(self):
        string = input('> Informe uma string: ')
        return string
    
class Consoante:

    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z','B', 'C', 'D', 'F', 'G','H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    
    def __init__(self):
        self._string = StringAlfa()

    def get_consoante(self):
        list_consoante =[]
        for i in self._string.get_string() :
            if i in self.consoantes:
              list_consoante.append(i)
        print("As consoantes lidas foram {} e a quantidade de consoante é {} " .format(list_consoante,len(list_consoante)))      


get = Consoante() 
get.get_consoante()  


