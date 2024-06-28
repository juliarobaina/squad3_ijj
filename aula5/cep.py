import requests

cep = input("Digite seu cep: ")

response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')

data = response.json()

print("Digite o que você quer ver no seu cep de acordo com as opções abaixo:")
for key in data.keys():
    print(f'{key}', end=' ')
    
print()
queroNoCep = input()
#print(data.keys())
print(data[queroNoCep])