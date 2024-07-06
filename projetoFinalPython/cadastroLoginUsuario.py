def criarUsuarioAPI(usuario: dict ) -> None:
    try:
        response = requests.post('https://desafiopython.jogajuntoinstituto.org/api/users/', data=usuario)
        #uma requisição malfeita (resposta que não tenha código 200), levanta uma exceção
        response.raise_for_status()
        print(f"Usuário {usuario['username']} criado com sucesso!")
    #pega erros HTTP
    except requests.exceptions.HTTPError as error:
        print("Erro:", error)

def salvarRespostaJson(response: dict) -> None:
    with open('respostaLoginUsuario.txt','w') as file:
        for key,value in response.items():
            file.write(key + ': ')
            file.write(value + '\n')

def logarUsuarioAPI(email: str, senha: str, nomeUsuario: str) -> None:
    try:
        response = requests.post('https://desafiopython.jogajuntoinstituto.org/api/users/login/', data={'email':email,'password':senha})
        response.raise_for_status()
        print(f"Usuário {nomeUsuario} logado com sucesso!")
        salvarRespostaJson(response.json())
    except requests.exceptions.HTTPError as error:
        print("Erro:", error)

import requests
from faker import Faker

#gerar dados falsos para ter um usuário falso
fake = Faker('pt_BR')
usuario = {
    'username': fake.user_name(),
    'email': fake.email(),
    'password': fake.password(),
    'phone': fake.phone_number(),
    'address': fake.address(),
    'cpf': fake.cpf()  
}

#para substituir a quebra de linha do endereço criado pela biblioteca faker por um hífen
splitAddress = usuario['address'].split('\n')
usuario['address'] = " - ".join(splitAddress)

print('Os dados do usuário criado foram')
for key,value in usuario.items():
    print(f'{key}: {value}')

criarUsuarioAPI(usuario)

logarUsuarioAPI(usuario['email'],usuario['password'],usuario['username'])