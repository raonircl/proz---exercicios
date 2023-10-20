def calculadora(num1, num2, op):
    if op == 1:
        result = num1 + num2
    elif op == 2:
        result = num1 - num2
    elif op == 3:
        result = num1 * num2
    elif op == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Erro na divisão'
    else:
        result = 0
    
    return result

num1 = 10
num2 = 2
op = 1

resultado = calculadora(num1, num2, op)
print("Resultado: ", resultado)

#outra forma de instanciar uma função
print(calculadora(num1, num2, op))