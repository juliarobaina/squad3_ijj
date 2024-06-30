#Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

# Solicitação de entrada de uma palavra (string)

palavra = input('Digite uma palavra para descobrir suas vogais: ')
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0
#Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
#Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.

for letra in palavra:
  if letra in vogais:
    print(f'Contém a letra {letra} ')
    contador += 1

#Imprima o número total de vogais na palavra.

print(f'O total de vogais na palavra é {contador}')