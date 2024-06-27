"""" 
Invés de uma maneira ordenada dos dados como Listas, Truplas

----Dicionários----

São uma maneira desordenada de organizar os dados (semelhante a organização de um Banco de Dados)
 - Em um dicionário usamos entre {} para delimitar
 - Também usamos {} para posicionar elemementos
 - separamos "valor/dados" por : e dentro desse "dado" pode conter listas/valores/nulo
"""

dicionario_de_registro = {

    'pessoa1' : {'nome': 'Annielle'},
    'pessoa2' : {'nome': 'Julia', 'idade': 25, 'profissao': 'Estudante e Analista nas horas vagas'},
    'pessoa3' : {},
    'pessoa4' : {'idade': 28, 'profissao': 'vivendo a vida na praia com sua arte'},
    'pessoa5' : {'nome': 'Vitor Back', 'idade': 23, 'profissao': 'Analista de Qualidade'},
    'pessoa6' : {'nome': 'Caio', 'idade': 26, 'profissoa': 'inspetor de qualidade'} 
}

dicionario_do_QA = {
    'nome' : {'Annielle'},
    'idade' : {'24 anos'},
    'profissao' : {'Desempregada'}
}

print(f'O dicionário da tarefa (como deveria ser): {dicionario_do_QA}\n\n\n')
print(f'Todo o dicionário: \n\n\n{dicionario_de_registro}\n\n\nSó da 1 pessoa: {dicionario_de_registro['pessoa1']}') #print pela chave da pessoa em questão
print(f'Terceira pessoa esqueceu do cadastro: {dicionario_de_registro["pessoa3"]}\nE a quarta esqueceu do nome: {dicionario_de_registro["pessoa4"]}')