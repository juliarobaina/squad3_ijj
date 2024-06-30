import requests

# Dicionário com nome e CEP dos integrantes do squad
squad = {
    "Tamires": "07179260",
    "Anielle": "58200000",
    "Caio": "41194105",
    "Vitor": "79009080",
    "Julia": "25268160"
}

# Itera sobre cada integrante do squad
for name, cep in squad.items():
    # Faz a requisição para o serviço ViaCep
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    # Converte a resposta para JSON
    data = response.json()
    
    # Exibe os dados retornados
    print(f'Nome: {name}')
    print(f'Localidade: {data["localidade"]}')
    print(f'CEP: {data["cep"]}')
    print('-' * 20)  # linha separadora entre os integrantes