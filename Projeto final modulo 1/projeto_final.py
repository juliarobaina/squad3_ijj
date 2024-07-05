import requests
import json

criar_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/"

login_usuario = "https://desafiopython.jogajuntoinstituto.org/api/users/login/"

data_usuario = {
    "username" : "Mario",
    "email" : "mario@hotmail.com",
    "password" : "123456786",
    "phone" : "12345678901",
    "cpf" : "003.456.789-00",
    "address" : "123 Main St, city, Country"
}


response = requests.post(criar_usuario, json=data_usuario)
if response.status_code == 201:
    print("Usuário criado com sucesso")
else:
    print(f"Falha ao criar usuário: {response.status_code}")
    print(response.json())


login_data ={
    "email" : data_usuario["email"],
    "password" : data_usuario["password"]
}

response = requests.post(login_usuario, json=login_data)
if response.status_code == 200:
    print("Login realizado com sucesso")
    login_response = response.json()



    with open("login_response.json", "w") as json_file:
        json.dump(login_response, json_file, indent=4)
    print("Resposta do login salva em 'login_response.json'.")
else:
    print(f"Falha ao realizar login: {response.status_code}")
    print(response.json())