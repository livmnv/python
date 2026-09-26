valor = []

for c in range(1, 6):
    peso = float(input('Digite o peso: '))
    valor.append(peso)

maior = max(valor)
menor = min(valor)

print(f'O maior peso foi {maior} kg')
print(f'O menor peso foi {menor} kg')