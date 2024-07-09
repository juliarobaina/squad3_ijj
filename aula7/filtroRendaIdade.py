import pandas as pd

dados = pd.read_csv('./dados_ficticios.csv')

'''
escrever o que faz em items
                    iterrows
                    tuples
'''

print(dados[dados['idade'] > 40])
print(dados[dados['renda'] > 5000])
print(dados[dados['renda'] > 15000])


