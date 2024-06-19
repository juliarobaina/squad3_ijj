nomePet = input("Digite o nome do seu cachorro: ")
idadeHumanaPet = int(input("Digite a idade humana do cachorro: "))
portePet = input("Digite se o cachorro tem porte grande, medio ou pequeno: ")
qtdBanhoPetAno = int(input("Digite quantos banhos por ano o cachorro tomou: "))

idadePet = idadeHumanaPet * 7
lucro = 0

if portePet == 'grande':
    lucro = (75 * qtdBanhoPetAno) - (20 * qtdBanhoPetAno)
    print(f"Olá, {nomePet} tem {idadePet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")

elif portePet == 'medio':
    lucro = (60 * qtdBanhoPetAno) - (15 * qtdBanhoPetAno)
    print(f"Olá, {nomePet} tem {idadePet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")

elif portePet == 'pequeno':
    lucro = (50 * qtdBanhoPetAno) - (5 * qtdBanhoPetAno)
    print(f"Olá, {nomePet} tem {idadePet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")

else:
    print("porte de pet inválido, tente novamente")



