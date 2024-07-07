from faker import Faker
import csv

def criar_personas(num_personas):
  faker = Faker('pt_BR')
  personas = []

  for _ in range(num_personas):
    persona = {
      'nome': faker.name(),
      'cidade': faker.city(),
      'idade': faker.random_int(min=18, max=60),
    }
    personas.append(persona)

  return personas

# função para criar o arquivo CSV
def salvar_personas_csv(personas, caminho_arquivo):
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nome', 'cidade', 'idade'])
        writer.writeheader()
        writer.writerows(personas)

# Defina o número de personas e o caminho do arquivo CSV
numero_de_personas = 10
caminho_csv = 'personas.csv'

# Crie e salve as personas
personas = criar_personas(numero_de_personas)
salvar_personas_csv(personas, caminho_csv)

print(f'{numero_de_personas} personas foram salvas em {caminho_csv}')