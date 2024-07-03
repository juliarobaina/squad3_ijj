import pandas as pd

# Lendo o arquivo CSV
dados = pd.read_csv('C:/BackEnd/squad3_ijj/atividade_IJJ/atividades_aula/dados_ficticios.csv')

# Criando o DataFrame
df = pd.DataFrame(data=dados)

# Imprimindo linhas onde a idade é maior ou igual a 40
print("Pessoas com idade >= 40:")
print(df[df['idade'] >= 40])

# Imprimindo linhas onde a renda é maior ou igual a 5000
print("\nPessoas com renda >= 5000:")
print(df[df['renda'] >= 5000])

# Imprimindo linhas onde a renda é maior ou igual a 15000
print("\nPessoas com renda >= 15000:")
print(df[df['renda'] >= 15000])