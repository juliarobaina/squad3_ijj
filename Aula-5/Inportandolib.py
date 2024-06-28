import requests

cep = input('Informe um CEP: ') 
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

data = response.json()

print(f':\n', 'Localidade:', 
      data['localidade'], data['cep'], data['logradouro'])

'cep': '79680-000', 'logradouro': '', 'complemento': '', 'unidade': '', 'bairro': '', 'localidade': 'Água Clara', 'uf': 'MS', 'ibge': '5000203', 'gia': '', 'ddd': '67', 'siafi': '9003'}