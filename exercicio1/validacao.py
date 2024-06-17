def validarNome(nomeUsuario):
    #se o nome que o usuário digitou não contém somente letras ou não respeita o tamanho mínimo e máximo de caracteres, ele deve responder novamente a pergunta
    while True:
        nomeSplit = nomeUsuario.split(" ")
        letra = True
        cont += 1
        for key in nomeSplit:
            if key.isalpha() != True:
                letra = False
                break

        if letra and len(nomeUsuario) > 1 and len(nomeUsuario) < 151:
            break
       
        nomeUsuario = input("Digite seu nome (mínimo de 2 caracteres e máximo de 150 caracteres): ")
        
    return nomeUsuario

def validarAltura(altura):
    #se a altura que o usuário digitou não está com a mesma estrutura do exemplo, ele deve responder novamente a pergunta
    while True:
        alturaSplit = altura.split(".")
        if len(alturaSplit) == 2:        
            if ( len(alturaSplit[0]) == 1 and  len(alturaSplit[1]) == 2): # len()-> O(1)
                if (alturaSplit[0].isnumeric() and alturaSplit[1].isnumeric()): #isnumeric()-> O(n)
                    break
        altura = input("Digite sua altura (como por exemplo 1.60): ")
    return altura

def validarIdade(idade):
    #se a idade que o usuário digitou não é um número positivo ou é zero, ele deve responder novamente a pergunta acima
    while True:
        if idade.isnumeric() and idade != "0":
            break
        idade = input("Digite sua idade (somente o número): ")
    return idade
