class Pessoa():
        def __init__(self, peso, nome, idade):
            self.nome=nome
            self.idade=idade
            self.peso=peso
            self.falando= False
            self.comendo= False
            self.dormindo= False
        def pararComer(self):
            if self.comendo == False:
                print(f"{self.nome}, não está comendo")
            else:
                print(f"{self.nome} parar de comer")
            self.comendo = False

        def pararFalar(self):
            if self.falando==False:
                print(f"{self.nome} não esta falando")
            else:
                print(f"{self.nome} ,para de falar")
            self.falando = False

        def pararDormir(self):
            if self.dormindo==False:
                print(f"{self.nome} não esta dormindo")
            else:
                print(f"{self.nome} parar de dormir")
            self.dormindo = False

        def comer(self,comida):
            if self.comendo== True:
                print(f"{self.nome} já esta comendo")
            elif self.falando == True:
                print(f"{self.nome} não pode  falar pois está comendo")
            else:
                print(f"{self.nome}, foi comer{comida}")
                self.comendo = True

        def dormir(self):
            if self.dormindo == True:
                print(f"{self.nome} está dormindo")
            elif self.comendo == True:
                print(f"{self.nome} não pode comer pois está dormindo")
            else:
                print(f"{self.nome} foi comer")
                self.comendo =True

        def falar(self):
            if self.falando == True:
                print(f"{self.nome} está falando")
            elif self.comendo ==True:
                print(f"{self.nome} já esta comendo, não pode falar")
            else:
                print(f"{self.nome} esta falando")
                self.comendo = True
