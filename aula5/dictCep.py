import requests

nomeCep = {
    'nome':('Julia','Annielle','Caio','Tamires','Vitor'),
    'cep':('25268160','58200000','41194105','07179260','79009080')
}


pos = 0
for nome in nomeCep['nome']:
    response = requests.get(f'http://viacep.com.br/ws/{nomeCep["cep"][pos]}/json/').json()
    
    print(f'Integrante: {nome} - Cidade: {response['localidade']} - Estado: {response['uf']} ')
    pos += 1

