import csv

carros = [
    ['Bmw', 'Gol', '2017'],
    ['VW', 'Virtus', '1999'],
    ['Fiat', 'Pálio', '2002'],
]

with open('carros.csv', 'w') as arquivo:
    fileCSV = csv.writer(arquivo, delimiter=';')

    fileCSV.writerow(['Marca', 'Modelo', 'Ano'])
    fileCSV.writerow(carros)