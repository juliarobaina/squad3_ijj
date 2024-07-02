import requests

cep = input("Digite o seu CEP (apenas números): ")

# Conjuntos de estados das regiões Norte e Nordeste
norte = {'AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'}
nordeste = {'AL', 'BA', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'}


def frete_gratis(cep):
  response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

  if response.status_code == 200:
    data = response.json()
    estado = data.get('uf')


    if estado in nordeste or estado in norte:
        print("Seu CEP é elegível para frete grátis na região Norte ou Nordeste.")
    else:
        print("Seu CEP não é elegível para frete grátis na região Norte ou Nordeste.")
  else:
       print('CEP inválido ou erro na consulta!')


# Chamar a função frete_gratis com o CEP fornecido
frete_gratis(cep)
     