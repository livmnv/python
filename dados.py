from random import randint
from time import sleep

soma_idade = 0
mulheres = 0
maior_idade_m = 0
nome_m_velho= ''

for c in range (1, 5):
    print (f'---- {c} Pessoa ----')
    nome= input('Qual seu nome? ')
    idade= int(input('Qual sua idade? '))
    sexo= input('Seu sexo: [M] OU [F] ').upper()
    print(' ' * 30)
    sleep(1)

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_m:
            maior_idade_m = idade
            nome_m_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres += 1

media_idade = soma_idade // 4

print(f'A média de idade do grupo é {media_idade}')
print(f'O homem mais velho é {nome_m_velho}')
print(f'Existem {mulheres} mulheres com menos de 20 anos')
    
    
    
    
    
    
    
    
    #i
    

    #if sexo = feminino and idade < 20:
    #    mulheres += 1
   
    #print (f'A media das idades e {media_idade}')