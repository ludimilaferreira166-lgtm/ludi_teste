class Pessoas:
    
   def __init__(self, nome, idade): 
    self.nome = nome 
    self.idade = idade

   def apresentar(self):
    print("Olá, meu nome é", self.nome)

class aluno:
    def estudar(self):
        print(self.nome, "está estudando")

class professor(Pessoas):

    def ensinar(self):
        print(self.nome, "está ensinando")