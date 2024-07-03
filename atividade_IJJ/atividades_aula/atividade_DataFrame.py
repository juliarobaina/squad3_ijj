import pandas as pd

dados = {
  'Nome': ['Tamires', 'Pedro', 'Bia', 'Solange','Tamara', 'Matheus', 'Ana'],
  'Idade': [30, 34, 40, 44, 20, 22, 28],
  'Cidade': ['Recife', 'São Paulo', 'Salvador', 'Recife', 'Salvador', 'Recife', 'Manaus']
}

df = pd.DataFrame(data=dados)

print(df['Idade'])

df_recife = df[df['Cidade'] == 'Recife']

print(df_recife)