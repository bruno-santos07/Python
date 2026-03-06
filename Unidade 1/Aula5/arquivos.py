arquivo = open('pessoas.txt', 'w')

arquivo.write('Bruno\n')
arquivo.write('Aline\n')
arquivo.write('John\n')

arquivo.close()

with open('pessoas.txt', 'r+') as arquivosLeitura:
    for linha in arquivosLeitura:
        print(linha)