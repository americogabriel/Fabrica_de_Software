
num1 = int (input("Digite um número: "))
num2 = int (input("Digite um número: "))
print("Operações: +(soma) -(subtração) *(multiplicação) /(divisão)")
operação = input("Digite um das operações: ").strip()


if operação == '*':
    print(f"O resultado da operação: {num1} * {num2} é: {num1 * num2} ")
elif operação == '+':
    print(f"O resultado da operação: {num1} + {num2} é: {num1 + num2} ")
elif operação == '-':
    print(f"O resultado da operação: {num1} - {num2} é: {num1 - num2} ")
elif operação == '/':
    print(f"O resultado da operação: {num1} / {num2} é: {num1 / num2} ")

else:
    print("Digite uma das operações válidas(+;-;/;*)")
