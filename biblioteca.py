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
class ContaBancaria():
    def __init__(self, numero, nome, tipo, saldo, limite):
        self.numero=numero
        self.saldo=0
        self.nome=nome
        self.tipo=tipo
        self.status=False
        self.limite= 0


    def ativarconta (self):
        if self.status == False:
            print("conta ativa c sucesso")
            self.status = True
        else:
            print("conta já está ativa")

    def statussDsativar(self):
        if self.status == False:
            print("conta desativada")
        else:
            print("desaativa")

    def desativarconta(self):
        if self.status == True:
            print("conta desativada c sucesso")
            self.status = False
        else:
            print("conta está desativada")

    def  verificarsaldo(self):

        print(f"o saldo é :{self.saldo}")

    def depositar(self, valor):
        self.saldo+=valor
        print(f"ficou {self.saldo}")

    def sacar(self,valor):
        if self.status == False:
            print("conta inativa,")
        else:
            if (self.saldo + self.limite) > valor:
                print("saldo negtivo, não pode sacar")
            else:
                self.saldo -= valor
                print("saque com sucesso")


    def ajustarlimite(self,limite):
        self.ajustarlimite = limite
        print(f"limite adicionado")
class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"o {self.nome} foi comer...")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f'o {self.nome} foi miando...')
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def comer(self):
        print(f'{self.nome} foi comer capim')

    def mugir(self):
        print(f'a {self.nome} está mugindo')
class Coruja(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def chirriar(self):
        print(f'a {self.nome} está chirriando')
class Porco(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def dormir(self):
        print(f'a {self.nome} está dormindo')
class Pintinho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def piar(self):
        print(f'{self.nome} está piando')
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'{self.nome} está latindo')
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f'{self.nome} foi comer cenoura')
class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'o valor do ingresso normal é: {self.valor}')
class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
        self.valor *= 1.5

class

