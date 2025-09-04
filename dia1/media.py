nota1 = float(input("Digite sua Primeira nota: "))
nota2 = float(input("Digite sua Segunda nota: "))
nota3 = float(input("Digite sua Terceira nota: "))
nome = input("Digite o nome do Aluno: ")


peso1 = nota1 * 2
peso2 = nota2 * 5
peso3 = nota3 * 6

media = (peso1 + peso2+ peso3) / 13

print(f"A média ponderada do aluno {nome} é: {media:.1f}")

