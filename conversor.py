numero = int(input("Digite um numero: "))
base = int(input("Escolha a base (1- binario, 2- octal ou 3- hexadecimal): "))

if base == 1:
    print(f"A conversão para binário é {bin(numero)}")

elif base == 2:
    print(f"A conversão para octal é {oct(numero)}")

elif base == 3:
    print(f"A conversão para hexadecimal é {hex(numero)}")