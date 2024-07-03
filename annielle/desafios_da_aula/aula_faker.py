from faker import Faker 

faker = Faker('pt_BR')

dicionario_faker = {
    'nome' : faker.name(),
    'endereço' : faker.address(),
    'idade' : faker.random_int(min=18, max=30)
}

print(dicionario_faker)

