pessoa = {'nome':'Gabriel'}
pessoa2 = {'nome':'Paulo'}

lista = [pessoa,pessoa2]

for person in lista:
    print(person['nome'])

pessoa['nome'] = 'Joao'
for person in lista:
    print(person['nome'])
print (pessoa)

pessoa2['idade'] = 13
for person in lista:
    print(person['nome'])
    if 'idade' in person:
        print(person['idade'])
