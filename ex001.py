#Definição de Classe
class Gafanhoto:
    def __init__(self): #Metodo construtor
        #Atributos de instancia
        self.nome = ""
        self.idade= 0

    #Metodos de instancia
    def aniversario(self):
        self.idade +=1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

#Definição de Objeto
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade= 17
g1.aniversario()
print(g1.mensagem())
g2 = Gafanhoto()
g2.nome = "José"
g2.idade= 71
g2.aniversario()
print(g2.mensagem())
