
#time = input('Digite seu time: ')

#if time == 'Corinthians':
#  print('Você é timão!')
#elif time == 'Bahia': # o elif pode sr repetido se tiver mais condições
 # print('Você é esquadrão!')
#else:
 # print('Você não é timão!')

match time:
  case "Corinthians":
    print("Você é timão!")
  case "Bahia":
    print("Você é esquadrão!")
  case "Gremio":
    print("Você é imortal!")
  case _:
    print("Quem não é não se mete")


#usuario = 16

#if usuario > 18:
# print('Indivíduo possui idade mínima para dirigir')
#elif usuario >= 17 and usuario <= 18:
#  print('Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir')
#else:
#  print('Indivíduo NÃO possui idade mínima para dirigir')