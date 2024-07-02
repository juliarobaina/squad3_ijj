import requests 

nordeste = {'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'}
norte = {'AC', 'AM', 'PA', 'RO', 'RR', 'TO'}
cep = int(input('Qual é o cep?\n'))

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = response.json()
estado = data.get('uf')
if estado in nordeste or norte:
    print('FRETE GRÁTIS')
else:
    print('não é do estado do Nordeste ou Norte')
