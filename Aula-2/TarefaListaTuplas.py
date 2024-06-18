campeoesWildRift = ("Urgot - Top", "Amummu - JG", "Zigs - Mid", "Leona - Sup", "Jhin - ADC")

listaCampeao = list(campeoesWildRift)

print(listaCampeao)

listaCampeao.extend(["Veigar - Mid", "Teemo - Top"])

print(listaCampeao)

listaCampeao.pop()

print(listaCampeao)

print(listaCampeao[0])

totalElementos = len(listaCampeao)

print(totalElementos)

dicionariofuncionarios={
    'Nome': 'Vitor Back', 
    'Idade': 26,
    'Profissão': 'Anal. de Qualidade',
    
}

nome = dicionariofuncionarios['Nome']
idade = dicionariofuncionarios['Idade']
profissao = dicionariofuncionarios['Profissão']

print(nome)