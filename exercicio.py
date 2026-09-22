nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if nome and idade:
    print (f'Seu nome e: {nome}')
    print (f'Seu nome invertido e: {nome[::-1]}')

    if ' ' in nome:
        print (f'Seu nome tem espaços')
    else: 
        print (f'Seu nome não tem espaços')

    print (f'Seu nome tem {len(nome)} caracteres')
    print (f'A primeira letra do seu nome e: {nome[0]}')
    print (f'A ultima letra do seu nome e: {nome[-1]}')
else:
    print("Por favor, insira um nome e uma idade válidos.")

    #nessa atividade aprendi a usar fatiamento, casefold, in, len e if else.