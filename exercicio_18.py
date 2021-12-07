"""
Implemente uma classe chamada Carro de acordo com as seguintes regras:
a. um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de
combustível no tanque;b. o consumo é especificado no construtor e o nível de combustível inicial é 0;
c. forneça um método andar( ) que simula o ato de dirigir o veículo por uma certa distância, reduzindo o
nível de combustível no tanque de gasolina;
d. forneça um método obterGasolina( ), que retorna o nível atual de combustível;
e. forneça um método adicionarGasolina( ), para abastecer o tanque.
"""




class Carro:
    def __init__(self) -> None:
        self.consumo = 10
        self.combustivel = 0
        

    def andar(self):
        km =  int(input('> Informe quantos kilometros ira percorrer: '))
        combustivel_consumido = km / self.consumo
        if combustivel_consumido >= self.combustivel:
           print("O nível atual de combustível atual não é suficiente. O nivel de combustivel é apenas {} ".format(self.combustivel))
        else:
            self.combustivel -= combustivel_consumido
        
    
    def obterGasolina(self,combustivel):
        self.combustivel = combustivel
        return combustivel
        
      
    
    def adicionarGasolina(self,combustivel):
        self.combustivel += combustivel
        return combustivel

go = Carro()
go.obterGasolina(10)
go.adicionarGasolina(10)
go.andar()
    
