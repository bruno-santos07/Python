class Imovel:
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self.nome = nome
        self.uf = uf
        self.uf = valor
        self.uf = endereco
        self.uf = area

    def detalhar(self):
        print(self.__dict__)


    def calcularImposto(self):
        return self.valor * 0.02

class ImovelResidecial(Imovel):
    def __init__(self, nome, uf, valor, endereco='', area=''):
        super().__init__(nome, uf, valor, endereco, area)
        self.quartos = 0
        self.piscina = False

class ImovelComercial(Imovel):
    ...

class ImovelRural: 
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = True
    
    def mesPlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 2: print('Soja')
            case other: print('Algoddão')

class Fazenda(Imovel, ImovelRural):
    ...

fazenda = Fazenda('Fazenda Modelo', 'GO', 1000000)
casa = ImovelResidecial('Minha casa', 'SP', 300000)
casa.detalhar()
print(fazenda.calcularImposto())
fazenda.mesPlantacao(7)
