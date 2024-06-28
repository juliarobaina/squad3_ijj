frutas = ["maçã", "caju", "mamão", "jabuticaba"]
alergias = ["frutose", "lactose", "glúten"]
alergias.append(frutas[-2])

for fruta in frutas:
    if fruta in alergias:
        print(fruta)