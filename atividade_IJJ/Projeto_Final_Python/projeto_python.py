import requests
from faker import Faker
import pandas as pd


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

# Função para criar usuário no endpoint
def create_user(user_data):
    url = 'https://desafiopython.jogajuntoinstituto.org/api/users/'
    response = requests.post(url, json=user_data)
    try:
        response.raise_for_status()  # Verifica se houve erro
        return response.json()
    except requests.exceptions.HTTPError as err:
        return {"error": str(err)}

# Função para fazer login com o usuário criado
def login_user(user_data):
    url = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'
    login_data = {
        "username": user_data["username"],
        "password": user_data["password"]
    }
    response = requests.post(url, json=login_data)
    try:
        response.raise_for_status()  # Verifica se houve erro
        return response.json()
    except requests.exceptions.HTTPError as err:
        return {"error": str(err)}

# Gerar dados de um único usuário
user_data = generate_user_data()

# Colocar o dicionário dentro de uma lista
df_user_data = pd.DataFrame([user_data])
print(df_user_data)

# Criar o usuário no endpoint
create_response = create_user(user_data)
print("Create User Response:", create_response)

# Fazer login com o usuário criado
login_response = login_user(user_data)
print("Login User Response:", login_response)