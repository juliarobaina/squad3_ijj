idade = int(input("Digite sua idade: "))

if idade > 18:
    print("Indivíduo possui idade mínima para dirigir")
elif idade == 17 or idade == 18:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else:
    print("Indivíduo NÃO possui idade mínima para dirigir")

time = "u"

match time: #igual switch case
    case 'b':
        print("b")
    case 'a':
        print("a")
    case _:# = default
        print("ola")