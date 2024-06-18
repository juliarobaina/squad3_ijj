pratos = ("cuzcuz", "tapioca", "arroz", "feijão", "bolo")
#print(f"tipo {type(pratos)} - valores {pratos}\n")

pratos = list(pratos)
#print(f"tipo {type(pratos)} - valores {pratos}\n")

pratos.append("cocada")
pratos.append("canjica")

#print(f"{pratos}\n")

primeiroPrato = pratos.pop(0)
ultimoPrato = pratos.pop()
print(f"Removido elemento da primeira posição {primeiroPrato}\n")
#print(f"Removido elemento da última posição {ultimoPrato}\n")

#print(f"{pratos}\n")

print(f"O tamanho da lista de pratos é {len(pratos)}\n")

dadosUsuario = {
    'nome' : 'Naruto',
    'idade' : 32,
    'profissao' : 'Hokage'
}

print(f"Nome do usuário: {dadosUsuario['nome']}")
