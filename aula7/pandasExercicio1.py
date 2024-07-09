import pandas as pd

dataset = {
    'nome': ('João','Maria','José','Carlos','Celma','Pedro','Felícia'),
    'idade': (23,34,45,56,67,78,89),
    'cidade': ('Recife','São Paulo','Salvador','Manaus','Recife','Recife','Salvador')
}

df = pd.DataFrame(data=dataset)
print(df)

pos = 0
print('Moradores de Recife')
for moraRecife in dataset['cidade']:
    if moraRecife == 'Recife':
        print(dataset['nome'][pos])
    pos += 1
print('-----------------------')
#outra versão disponibilizada por colega para estudo
for ind,linha in df.iterrows():
    if linha['cidade'] == 'Recife':
        print(linha['nome'])
print("----------------------------")
#outra versão
print(df[df['cidade'] == 'Recife'])