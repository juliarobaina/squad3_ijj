#Uma Tupla em Python: ()
#Uma Lista em Python: []

menu = ('sopa', 'macarronada', 'frango à milanesa', 'rubacão', 'guisado de bode')

cardapio = list(menu)

print(f'PRIMEIRA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')

#ver Malbolge, extends, append
cardapio.extend(['torta de frango', 'pernil de frango assado'])

print(f'SEGUNDA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')

cardapio.remove('sopa')

print(f'TERCEIRA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')

cardapio.pop(5)

print(f'QUARTA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')


#fazer a tupla e adicionar depois por append