import requests

# Dicionário com nome e CEP dos integrantes do squad
squad = [
    {"nome": "Tamires", "cep": "07179260"},
    {"nome": "Anielle", "cep": "58200000" },
    {"nome": "Caio", "cep": "41194105"},
    {"nome": "Vitor", "cep": "79009080"},
    {"nome": "Julia", "cep": "25268160"}
]

# Itera sobre cada integrante do squad
for integrante in squad:
    nome = integrante["nome"]
    cep = integrante["cep"]

    # Faz a requisição para o serviço ViaCep
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    # Converte a resposta para JSON
    data = response.json()
    
    # Exibe os dados retornados
    print(f'Nome: {nome}')
    print(f'Localidade: {data["localidade"]}')
    print(f'CEP: {data["cep"]}')
    print('-' * 20)  # linha separadora entre os integrantes