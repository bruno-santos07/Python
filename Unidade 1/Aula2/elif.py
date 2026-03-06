receberNota1 = float(input('Digite uma nota: '))
receberNota2 = float(input('Digite uma nota: '))
receberNota3 = float(input('Digite uma nota: '))
receberNota4 = float(input('Digite uma nota: ')) 

print('nota digitada:', receberNota1)
print('nota digitada:', receberNota2)
print('nota digitada:', receberNota3) 
print('nota digitada:', receberNota4)

soma = receberNota1 + receberNota2 + receberNota3 + receberNota4
media = soma/ 4

print('A media é:', media)
if media >= 7:
    print('Aprovado')
elif media < 5:
    print('Reprovado!')
else:
    print('Em recuperação!')