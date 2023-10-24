def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if a == 0 or b == 0:
        return "Erro"
    return a / b

while True:
    print("Escolha a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    
    op = input("Digite o número da operação:")
    
    if op == "0":
        print("Até mais!")
        break
    elif op in ("1","2","3","4"):
        a = float(input("Digite o primeiro valor"))
        b = float(input("Digite o segundo valor"))
        
        if op == "1":
            resultado = soma(a, b)
            print("Resultado da soma: {resultado}")
        
        elif op == "2":
            resultado = subtracao(a, b)
            print("Resultado da subtração: {resultado}")
        
        elif op == "3":
            resultado = multiplicacao(a, b)
            print("Resultado da multiplicação: {resultado}")
            
        elif op == "4":
            resultado = divisao(a, b)
            print("Resultado da divisão:")
        
        else:
            print("Essa operação não existe.")
            
    else:
        print("Essa operação não existe.")
        