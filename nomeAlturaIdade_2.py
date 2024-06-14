nomeUsuario = input("Digite seu nome: ")
aux = True
#se o nome que o usuário digitou não contém somente letras, ele deve responder novamente a pergunta
while aux:
    if nomeUsuario.isalpha() and len(nomeUsuario) > 1:
        break
    nomeUsuario = input("Digite seu nome: ")


altura = input("Digite sua altura, como por exemplo 1.60: ")

while(aux):
    alturaSplit = altura.split(".")
    if len(alturaSplit) == 2:        
        if ( len(alturaSplit[0]) == 1 and  len(alturaSplit[1]) == 2): # len()-> O(1)
            if (alturaSplit[0].isnumeric() and alturaSplit[1].isnumeric()): #isnumeric()-> O(n)
                break
    #se o nome que o usuário digitou não está com a mesma estrutura do exemplo, ele deve responder novamente a pergunta
    altura = input("Digite sua altura, como por exemplo 1.60: ")

idade = input("Digite sua idade, somente o número: ")
#se o nome que o usuário digitou não é um número positivo, ele deve responder novamente a pergunta acima
while(aux):
    if idade.isnumeric() and idade != "0":
        break
    idade = input("Digite sua idade, somente o número:")

print(f"Seu nome é {nomeUsuario}, sua altura é {altura}m e você tem {idade} anos.")