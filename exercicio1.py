from biblioteca import Pessoa

'''aluno01= Pessoa (78, "Mari", 20 )
print(aluno01.peso)
print(aluno01.nome)
print(aluno01.idade)
print()

aluno01.comer("cachorro-quente")
aluno01.falar()
aluno01.dormir()
'''

from biblioteca import ContaBancaria
pessoa1 = ContaBancaria (2, "maria", "corrente", 400,500)

pessoa1.ativarconta()
pessoa1.depositar(1000)
pessoa1.ajustarlimite(1000)
pessoa1.sacar(1500)
pessoa1.verificarsaldo()
pessoa1.depositar(200)
pessoa1.verificarsaldo()

