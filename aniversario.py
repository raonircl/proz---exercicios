def calcular_idade(ano_nascimento):
    ano_atual = 2023
    idade = ano_atual - ano_nascimento
    return idade

while True:
    nome = input("Digite o seu nome completo: ")
    
    try:
        ano_nascimento = int(input("Digite o seu ano de nascimento que seja entre(1922-2021):"))
        
        if 1922 <= ano_nascimento <= 2021:
            idade = calcular_idade(ano_nascimento)
            print(f"{nome} tem {idade} anos de idade.")
            break
        else:
            print("Ano de nascimento inválido.")
            
    except ValueError:
        print("Ano de nascimento inválido.")