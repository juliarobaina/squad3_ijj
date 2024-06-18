#Crie uma tupla com 5 dados
animais = ('gato', 'cachorro', 'passaro', 'cavalo', 'carneiro')

#Altere a tupla para uma lista
animais_lista = list(animais)

print(animais_lista)

#Insira 2 dados extras a essa lista

animais_lista.append('tigre')
animais_lista.append('elefante')

print(animais_lista)

#Remova o primeiro dado da lista
animais_lista.pop(0)

print(animais_lista)

#Remova o último dado da lista
animais_lista.pop(5)

print(animais_lista)

#Faça um print com o primeiro dado da lista
print(animais_lista[0])

#Faça um print com a quantidade de dados da lista
quantidade = len(animais_lista)
print(quantidade)

# Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
pessoa = {"nome": "Caique", "Idade": 17, "Altura": 1.7}

#Imprima somente o valor contido na chave Nome do dicionário 

print(pessoa['nome'])