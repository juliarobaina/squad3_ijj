import os

# Lista de dado
dados = ['Professor', 'Médico', 'Eletricista']

# Variável com o nome do diretório
diretorio = 'diretorio_os'

# Comando para criar o diretório (O parâmetro 'exist_ok=True' impede que ocorra um erro se o diretório já existir.)
os.makedirs(diretorio, exist_ok=True)

# Criar nome do arquivo
nome_arquivo = os.path.join(diretorio, 'arquivo.txt')

# Abrir o arquivo no modo escrita e escreve os dados
with open(nome_arquivo, 'w') as arquivo:
  for linha in dados:
    arquivo.write(linha + '\n')

# Imprimir a localização do arquivo criado
print(f'Dados salvos em {nome_arquivo}')