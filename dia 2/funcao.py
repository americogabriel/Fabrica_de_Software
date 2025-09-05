def calcular(num1,num2,op):
    resultados = []
    while(True):
       
        if op == '+':
            result = num1 + num2
            resultados.append(result)
            print(f"O resultado da soma é: {result}")
        elif op == '*':
            result = num1 * num2
            resultados.append(result)
            print(f"O resultado da multiplicação é: {result}")
        elif op == '/' and num2 != 0:
            result = num1 / num2
            resultados.append(result)
            print(f"O resultado da divisão é: {result}")
        elif op == '-':
            result = num1 - num2
            resultados.append(result)
            print(f"O resultado da subtração é: {result}")
        else:
            print("Digite uma operação válida")
            break
        continuar = input("Deseja continuar com as operações?(S/N) ").strip().upper()
        if continuar not in ['S','SIM']:
            print(f"Os resultados de suas operações foram: {resultados}")
            break
        else:
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))
            print("Operações Disponíveis: soma(+),subtração(-),divisão(/),multiplicação(*)")
            op = input("Digite a sua operação desejada: ")


num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))
print("Operações Disponíveis: soma(+),subtração(-),divisão(/),multiplicação(*)")
op = input("Digite a sua operação desejada: ")

calcular(num1,num2,op)
                