import requests
from faker import Faker

fake = Faker('pt_BR')
usuario = {
    'username': fake.user_name(),
    'email': fake.email(),
    'password': fake.password(),
    'phone': fake.phone_number(),
    'address': fake.address(),
    'cpf': fake.cpf()
    
}

splitAddress = usuario['address'].split('\n')
usuario['address'] = " - ".join(splitAddress)

print('Os dados do usuário criado foram')
for key,value in usuario.items():
    print(f'{key}: {value}')

urlCriarUsuario = 'https://desafiopython.jogajuntoinstituto.org/api/users/'

try:
    response = requests.post(urlCriarUsuario, data=usuario)
    print(response.raise_for_status())
    print(f"Usuário {usuario['username']} criado com sucesso!")

except requests.exceptions.HTTPError as error:
    print("Erro:", error)

login = {
    'email': usuario['email'],
    'password': usuario['password']
}
urlLoginUsuario = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'

try:
    response = requests.post(urlLoginUsuario, data=login)
    response.raise_for_status()
    print(f"Usuário {usuario['username']} logado com sucesso!")

except requests.exceptions.HTTPError as error:
    print("Erro:", error)

with open('respostaLoginUsuario.txt','w') as file:
    for key,value in response.json().items():
        file.write(key + ': ')
        file.write(value + '\n')

#remover quebra de linha
#cadastrar usuário
#logar usuário
#salvar login json no arquivo