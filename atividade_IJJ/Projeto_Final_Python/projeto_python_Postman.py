from faker import Faker
import pandas as pd

# Criação da instância Faker configurada para português do Brasil
fake = Faker('pt_BR')

# Função para criar dados do usuário
def generate_user_data():
    user_data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "cpf": fake.cpf(),
        "password": fake.password()
    }
    return user_data

# Gerar dados de um único usuário
user_data = generate_user_data()

# Colocaquei o dicionário dentro de uma lista
df_user_data = pd.DataFrame([user_data])  
print(df_user_data)

df_user_data.to_csv('user_list.csv', index=False)

