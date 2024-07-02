import requests 

nordeste = {'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'}
norte = {'AC', 'AM', 'PA', 'RO', 'RR', 'TO'}
sudeste= {'ES', 'MG', 'SP', 'RJ'}
centroOeste = {'GO', 'MS', 'MT'}
sul = {'RS', 'PR', 'SC'}

def freteGratuito(valorCompra, estado):
    match valorCompra:
        case x if valorCompra >= 1 and estado in nordeste or estado in norte:
            print('FRETE GRÁTIS POR LOCALIDADE')
        case x if valorCompra > 50 and estado in sudeste or estado in sul:
            print('FRETE GRÁTIS POR COMPRA')
        case x if valorCompra > 80 and estado in centroOeste:
            print('FRETE GRÁTIS POR COMPRA')
        case _:
            print('Não está elegível para frete grátis')
            

cep = input('Qual é o cep?\n')
valorCompra = int(input('Quanto foi o valor da sua compra?'))

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
data = response.json()
estado = data.get('uf')

freteGratuito(valorCompra,estado)

print(f'Status code', response.status_code)
