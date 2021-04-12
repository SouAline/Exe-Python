peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = ((peso *100)/ (altura**2)) * 100
print(f'Seu imc é de {imc:.0f}')
#calculando imc