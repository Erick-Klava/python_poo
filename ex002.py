#Definição de Classe
class Gafanhoto:
    """ é assim que vc faz uma documentação de alguma coisa ,use print(x.__doc__) pra ler recomendado em codigos complexos
    """
    def __init__(self, nome = "", idade = 0): #Metodo construtor
        #Atributos de instancia
        self.nome = nome
        self.idade= idade

    #Metodos de instancia
    def aniversario(self):
        self.idade +=1

    def __str__(self):
        # substituimos o def mensagem(self) com o return igual pra facilitar a hora de printar e ficar um codigo mais clean
        #sem print(gx.mensagem) só print(gx)
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    def __getstate__(self):
        return f"Estado: Nome = {self.nome} , idade = {self.idade}"
#Definição de Objeto
g1 = Gafanhoto("Maria",17)
g1.aniversario()
print(g1)
print(g1.__doc__)
print(g1.__dict__)#ATRIBUTO
print(g1.__getstate__())#METODO ,É CUSTOMIZAVEL COMO FEITO ACIMA
print(g1.__class__)
