import math
parede = float(input('Quantos metros quadrados tem a área a ser pintada: '))
cobertura_tinta = 18 * 3 #ela cobre 54
cobertura = math.ceil(parede / cobertura_tinta)
total_tinta = 80 * cobertura
valor_total = cobertura * cobertura_tinta * total_tinta
print(f'Você precisará de {cobertura} latas de tinta no valor total de {total_tinta:.2f}')


'''n = float(input('Adicione em metros quadrados o tamanho da sala: '))
tinta_uso = n/3
preço_tinta = 80/18
print(f'Você deverá comprar {tinta_uso:.2f} litros de tinta.')
print(f'Você usará um total de {tinta_uso/18:.2f} balde de tinta')
print(f'Com valor total de {preço_tinta*tinta_uso:.2f}$')'''
#outra maneira de executar o codigo
