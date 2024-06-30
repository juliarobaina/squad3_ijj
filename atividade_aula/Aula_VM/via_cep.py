import requests

# Defina o CEP que você quer consultar
cep = input('Informe o seu cep sem pontos ou traços: ')

# Faça a requisição para o serviço ViaCep
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

data = response.json()

  # Exiba os dados retornados
print(f'Localidade: {data['localidade']}\nCEP: {data['cep']}\nLogradouro: {data['logradouro']}')
