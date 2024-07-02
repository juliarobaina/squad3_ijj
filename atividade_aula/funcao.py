numero_matricula = int(input(f'Digite o número da sua matricula: '))

def par_impar(matricula):

  if matricula % 2 == 0:
      return 'VOCÊ ESTÁ NO TIME AZUL'
  else:
      return 'VOCÊ ESTÁ NO TIME AMARELO'

mensagem = par_impar(numero_matricula)
print(mensagem)