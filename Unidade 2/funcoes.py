def dividir(n1,n2):
    if n2 == 0:
        print('Não é possivel dividir por zero!')
    else:
        resultado = n1/n2
    #print(f'O resultado  da divisão é {resultado}')
    return resultado
    

divisao = dividir(5, 80)
print('O resultado da divisão é:', divisao)

resultado = dividir(5, 5)
soma = 20 + resultado
print('A soma é', soma)

dividir(6,3)
