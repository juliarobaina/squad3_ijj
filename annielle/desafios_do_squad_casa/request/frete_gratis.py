import requests 

nordeste = {'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'}
cep = int(input('Qual é o cep?\n'))

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = response.json()
estado = data.get('uf')
if estado in nordeste:
    print('achamos!')


"""def nada(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    cepString = 'f{cep}'
    return cepString

def validaCEPNordeste(response):
    estado = response.get('uf')
    if estado in nordeste:
        print ('ok')

validaCEPNordeste(cep)"""
"""
print(f'Status code', response.status_code)
data = response.json()
match func:
    case cep == '83':
        print('print')
    case case2:
        print(f'Dados da Localidade: {data['localidade']} - {data['uf']}')"""