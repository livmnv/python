num = int(input('Digite um numero para receber a tabuada desse numero: '))
for numero in range (1, 11):
    resultado = num * numero
    print(f'{num} x {numero} = {resultado}')