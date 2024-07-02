import requests 

nordeste = {'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'}
norte = {'AC', 'AM', 'PA', 'RO', 'RR', 'TO'}

def fretegratuito (estado):
    if estado in nordeste or estado in norte:
        print('FRETE GRÁTIS')
    else:
        print('não é do estado do Nordeste ou Norte')

cep = input('Qual é o cep?\n')

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = response.json()
estado = data.get('uf')

fretegratuito(estado)
annielle = 58200000
julia = 25268160
