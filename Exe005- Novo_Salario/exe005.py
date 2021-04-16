salario = float(input('Qual o valor do salário R$ '))
reajuste = float(input('O percentual de aumento é de: '))
print(f'O novo salario com o aumento de {reajuste} é  de {(salario * reajuste)/100 +salario}')
