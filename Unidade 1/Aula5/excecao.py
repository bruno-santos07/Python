'''
try:
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))

    resultado = n1 / n2
    print(f'O resultado é {resultado}')

except Exception as erro:
    print(f'Ocorreu um erro: {erro}')
'''

try:
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))

    resultado = n1 / n2
    print(f'O resultado é {resultado}')

except ValueError:
    print('Digite apenas números')
except ZeroDivisionError:
    print('Não é possivel dividir por 0')

else:
    print('O programa foi executado corretamente')

finally:
    print('Fim')
