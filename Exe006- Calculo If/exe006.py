peso = float(input('Quantos kg de peixe foi pescado hoje?: '))
if peso <= 50:
    print('Muito bem, não precisará pagar multa hoje!')
else:
    print('Você pescou além do limite, precisará pagar {} de multa'. format((peso - 50)*4))

'''n1 = float(input('Adicione o KG'))

if n1 <= 50:
    print('Não paga multar')
    print('Total de 0,00$')

else:
    print('Multa por excesso de peso acima do permitido')
    n2 = n1 - 50
    n3 = n2 * 4
    print(f'Total de {n3}$')''' # Segunda maneira de fazer