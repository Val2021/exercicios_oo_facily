"""
Implemente a classe Funcionário com um nome e um salário. Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Crie o método aumentar_salario(percentual_aumento) que aumente o salário do funcionário em uma certa porcentagem. Escreva um pequeno programa que teste sua classe. 

"""
class Funcionario:
    def __init__(self) -> None:
        self.nome = ""
        self.salario = 0
    
    def aumentar_salario(self):
        self.nome = input("Digite o nome do funcionário: ")
        self.salario = int(input("Digite o salário de {} : " .format(self.nome)))
        porcentagem  = int(input("Digite uma porcentagem: "))
        self.novo_salario = (self.salario * (porcentagem /100)) + self.salario
        return self.novo_salario

    def show_salario(self):
        print("O novo salario de {} é {}" .format(self.nome,self.novo_salario))

app = Funcionario()
app.aumentar_salario()
app.show_salario()