preço = (float(input('Qual o valor do litro do combustivel?: ')))
dinheiro = (float(input('Quantos reais você possui para abastecer: ')))
print(f'Você pode abastecer {(dinheiro/preço):.2f} litros de gasolina com R$',dinheiro)