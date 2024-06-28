def qtdVogais(palavra):
    vogais = ('a','e','i','o','u')
    cont = 0

    for p in palavra:
        if p in vogais:
            cont += 1
    return cont

palavra = input("Digite uma palavra: ")

print(f"O total de vogais na palavra '{palavra}' é {qtdVogais(palavra)}")