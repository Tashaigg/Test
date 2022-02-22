from datetime import datetime
class Funcionarios:    
    def __init__ (self, nome, sobrenome, data, ano):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data = data
        self.ano = ano

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade(self):
        ano_atual = datetime.now().year
        self.anos = int(ano_atual - self.ano)
        return self.anos

usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009', 2009)
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005', 2005)

'''usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.data = '12/01/2009'

usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data = '15/10/2005' '''

print(usuario2.nome_completo())
print(usuario1.idade())
