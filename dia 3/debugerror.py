def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

try:
    notas = []
    for x in range(0,4):
        nota = int(input("Digite sua nota: "))
        notas.append(nota)
    media = calcular_media(notas)
    print(f"Média: {media:.2f}")
except Exception as erro:
    print(f'Deu esse erro ai: {erro}')