from faker import Faker

faker = Faker('pt_BR')

persona = {
  'nome': faker.name(),
  'idade': faker.random_int(min=18, max=60),
  'data': faker.date_of_birth(),
  'endereco': faker.address()
}

print(persona)