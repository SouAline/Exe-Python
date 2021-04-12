print('Digite as notas do aluno')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
media_ponderada = ((nota1*1)+(nota2*2)+(nota3*3))/(1+2+3)
print('A média ponderada do aluno foi de {:.2f}'.format(media_ponderada))
# Média ponderada é a soma de cada multiplicação da nota pelo seu peso e a divisão pela soma dos pesos.