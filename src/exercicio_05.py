"""
Faça um Programa que leia as idades e alturas de 10 alunos e determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
1. class Aluno:
2. funçao determinar alunos com mais de 13 anos
3. função determinar altura
4. função calcular media
"""


QTD_ALUNOS = 10
ALUNOS = []
class Aluno:
    def __init__(self,idade:int,altura:float) -> None:
        self.idade = idade
        self.altura = altura

    def get_idade(self):
        return self.idade
    
    def get_altura(self):
        return self.altura
    
    def set_idade(self,idade):
        self.idade = idade
    
    def set_altura(self,altura):
        self.altura = altura

class ListaAlunos:
    def __init__(self) -> None:
        self.alunos = []

    def insere_aluno(self,aluno):
        self.alunos.append(aluno)
    
    def media_altura(self):
        list_altura = []
        for aluno in self.alunos:
            altura = aluno.get_altura()
            list_altura.append(altura)
        media = sum(list_altura)/len(list_altura)
        return media
        
            
    def maior_treze(self):
        resultado = 0
        for aluno in self.alunos:
            if aluno.get_idade() >= 13:
                if aluno.get_altura() < self.media_altura():
                   resultado += 1
        print("A quantidade de  alunos com mais de 13 anos que possuem altura inferior à média da altura  dos alunos e :", resultado)


    
if __name__ == "__main__":
    lista_alunos = ListaAlunos()
    for i in range(QTD_ALUNOS):
        idade = int(input('> Informe a idade do aluno {}: ' .format(i + 1)))
        altura = int(input('> Informe a altura do aluno {}: ' .format(i + 1)))
        aluno = Aluno(idade,altura)
        lista_alunos.insere_aluno(aluno)
    lista_alunos.maior_treze()
    