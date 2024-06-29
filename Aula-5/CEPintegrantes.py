import requests

dado_integrantes = [{
    "Integrante": "Anielle", 
    "CEP":"58200000",
},
{
    "Integrante": "Caio", 
    "CEP":"79009090",
},
{
    "Integrante": "Julia", 
    "CEP":"25268160",
},
{
    "Integrante": "Tamires", 
    "CEP":"79680000",
},
{
    "Integrante": "Vitor", 
    "CEP":"79009080",
}]

for indice, integrante in enumerate(dado_integrantes):
    response = requests.get(f'https://viacep.com.br/ws/{integrante["CEP"]}/json/')

    data = response.json()

    print(f'Nome:', integrante['Integrante'], '\nCidade:', data['localidade'],"\n""########################")