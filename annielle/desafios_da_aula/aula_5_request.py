import requests 

cep = int(input('Qual é o cep?\n'))

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(f'Status code', response.status_code)
data = response.json()
print(f'Dados da Localidade: {data['localidade']} - {data['uf']}')