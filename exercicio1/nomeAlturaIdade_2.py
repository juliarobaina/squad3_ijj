import validacao

nomeUsuario = input("Digite seu nome (mínimo de 2 caracteres e máximo de 150 caracteres): ")
nomeUsuario = validacao.validarNome(nomeUsuario)

altura = input("Digite sua altura (como por exemplo 1.60): ")
altura = validacao.validarAltura(altura)

idade = input("Digite sua idade (somente o número): ")
idade = validacao.validarIdade(idade)

print(f"Seu nome é {nomeUsuario}, sua altura é {altura}m e você tem {idade} anos.")