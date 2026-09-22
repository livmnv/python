from datetime import date
atual = date.today().year

ano = int(input("Digite o ano do seu nascimento: "))
idade = atual - ano
if idade == 18:
    print("Voce pode se alistar")
elif idade > 18:
    print(f"Voce ja deveria ter se alistado ha {idade - 18} anos")
elif idade < 18:
    print("Voce ainda nao pode se alistar")
    print(f"Faltam {18 - idade} anos para poder se alistar")
