import os
import requests


integrantes = {
    "Caio" : "41194-105",
    "Vitor Back" : "79009-080",
    "Anielle" : "58200-000",
    "Julia" : "25268-160",
    "Tamires" : "07179-260"
}

diretorio = "cep_squad"
os.makedirs(diretorio, exist_ok=True)

nomeArquivo = os.path.join(diretorio, 'cep_integrantes.txt')
with open (nomeArquivo, "w") as arquivo:
    for nome, cep in integrantes.items():
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = response.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        arquivo.write(f"Nome: {nome}, Cidade: {cidade}\n")
        print(f"Nome:{nome}, Cidade: {cidade}") 
print(f"Dados salvos em {nomeArquivo}") 