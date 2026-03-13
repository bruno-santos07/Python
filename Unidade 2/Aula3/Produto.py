class Produto:
    def __init__(self, nome, valor, quantidade = 0, marca = '', modelo = ''):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.marca = marca
        self.modelo = modelo

    def vender(self, quantidade):     
        self.quantidade -= quantidade
        if(quantidade > self.quantidade):
            print('**********************')
            print('Não Há estoque suficiente')
            print('Quantidade máxima:', self.quantidade)
            print('**********************')
        else:
            self.quantidade -= quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade


produto1 = Produto('Celular', 2000, 10, 'Sansung', 'J11')
produto1.comprar(10)
produto1.vender(21)

print(produto1.__dict__)
