# programa de emprestimo bancario

valor= float (input ('Qual o valor do emprestimo?'))
salario= float (input ('Digite seu salario:'))
anos = int (input ('Em quantos anos voce pretende pagar?'))

prestacao = valor / (anos * 12)
minimo = salario * 30 / 100

print (f'O valor minimo da prestacao com base no seu salario e de R${minimo:.2f}')

if prestacao > salario * 0.3:
        print ('Emprestimo negado! A prestacao de R${:.2F} excede a margem de 30% do seu salario'.format(prestacao))
elif prestacao <= salario * 0.3:
        print ('Emprestimo aprovado!')
        