# Coletando a idade humana do pet
idade_humana = int(input("Digite a idade humana do seu pet: "))

# Calculando a idade do pet em anos de cachorro
idade_cachorro = idade_humana * 7

# Solicitando o porte do cachorro
porte = input("Digite o porte do seu cachorro (grande, médio ou pequeno): ").strip().lower()

# Solicitando o número de banhos em 12 meses
num_banhos = int(input("Digite o número de banhos que seu cachorro tomou nos últimos 12 meses: "))

#  Preços e custos por banho usando dicionários
precos = {
    "grande": 75,
    "médio": 60,
    "pequeno": 50
}

custos = {
    "grande": 20,
    "médio": 15,
    "pequeno": 5
}




# Calculando o lucro por banho
preco_banho = precos[porte]
custo_banho = custos[porte]
lucro_banho = preco_banho - custo_banho

# Calculando o lucro total em 12 meses
lucro_total = lucro_banho * num_banhos

# Exibindo a idade do pet e o lucro total
print(f"Olá, seu pet tem {idade_cachorro} anos em anos de cachorro e nos últimos 12 meses o lucro com este animal foi de R${lucro_total}")

