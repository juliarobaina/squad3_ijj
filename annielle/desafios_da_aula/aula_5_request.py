import requests

cep = input ('Qual é o cep?\n')

response = requests.get(f'https://viacep.com.br/ws/01001000/json/')
print(f'Status code', response.status_code)
data = response.json()
print('dados', 'dados[logradouro]')