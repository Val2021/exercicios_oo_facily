"""
Faça um programa completo utilizando classes e métodos que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro
iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade
de litros que foi colocada no veículo
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra
o valor a ser pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. c.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na
bomba.

"""

class BombaCombustivel:
    def __init__(self,tipoCombustivel: str,valorLitro:float,quantidadeCombustivel:float) -> None:
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    
    def abastecerPorValor(self,valor ) -> None:
        qtd_combustivel = valor / self.valorLitro
        self.alterarQuantidadeCombustivel(qtd_combustivel) 
        print("A quantidade de combustive colocada é {}" .format(qtd_combustivel))



    def abastecerPorLitro(self,qtd_litros )  -> None:
        valor_combustivel = qtd_litros * self.valorLitro
        self.alterarQuantidadeCombustivel(qtd_litros) 
        print("A quantidade de combustive colocada é {}" .format(valor_combustivel))
        

    def alterarValor(self,valorLitro)  -> None:
        self.valorLitro = valorLitro
        
        

    def alterarCombustivel(self,tipoCombustivel) -> None:
        self.tipoCombustivel = tipoCombustivel
        
    
    def alterarQuantidadeCombustivel(self,quantidadeCombustivel ) -> None:
        self.quantidadeCombustivel -= quantidadeCombustivel

bomba = BombaCombustivel("Gasolina",10,20)
bomba.abastecerPorValor(5)
bomba.abastecerPorLitro(2)
bomba.alterarValor(15)
bomba.alterarCombustivel("Alcool")
bomba.alterarQuantidadeCombustivel(100)


