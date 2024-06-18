#Uma Tupla em Python: ()
#Uma Lista em Python: []

cardapio = ['sopa', 'macarronada', 'frango à milanesa', 'rubacão', 'guisado de bode', 'torta de frango', 'pernil de frango assado']

print(f'PRIMEIRA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')

cardapio.remove('sopa')

print(f'SEGUNDA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')

cardapio.pop(5)

print(f'TERCEIRA VERSÃO \nO cárdapio possui {len(cardapio)} pratos, sendo eles: {cardapio}')
