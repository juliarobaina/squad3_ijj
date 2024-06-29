import os

username = os.environ.get('USERNAME')
print(f"Username: {username}")

diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")

os.mkdir('novo_diretorio')

'''if not os.path.isfile('novo_diretorio/teste.txt'):
    print('arquivo não existe')
else:'''
numList = [1,2,3,4,5,6,7,8,9]
with open('novo_diretorio/teste.txt','a') as arquivo:
    for num in numList:
        arquivo.write(str(num))

with open('novo_diretorio/teste.txt','r') as arquivo:
    print(arquivo.read())