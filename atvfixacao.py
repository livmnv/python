saldo = float(input('Digite o saldo da SUA CONTA: '))
valor_sacado = float(input('Digite o valor que deseja sacar:'))

if valor_sacado > saldo:
    print("Saldo insuficiente")
    
elif valor_sacado == saldo:
    print("Voce sacou todo o valor da suaa conta")
else:
    print("Valor sacado com sucesso")