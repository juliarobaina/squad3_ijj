# Criar uma tupla com 5 dados
tupla = ('dado1','dado2','dado3', 'dado4', 'dado5')

# Alterando a tupla para uma lista
lista = list(tupla)

# Inserindo 2 dados extras na lista
lista.append('dados6')
lista.append('dados7')

# Removendo o primeiro dado da lista
lista.pop(0)

# Remova o último dado da lista
lista.pop()

# Print com o primeiro dado da lista
print("Primeiro dado na lista", lista[0])

# Print com a quantidade de dados da lista
print("Quantidade de dados na lista:", len(lista))

# Criando um dicionário com os seguintes dados: Nome, Idade, Profissão
dicionario = {
    'Nome': 'Joao',
    'Idade': 30,
    'Profissão' : 'Engenheiro'
}

# Print do valor contido na chave Nome do dicionário
print("Nome no dicionário:", dicionario['Nome'])