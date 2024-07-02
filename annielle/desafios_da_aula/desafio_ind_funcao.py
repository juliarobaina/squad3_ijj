def defineTime(matricula):
    if matricula % 2 == 0:
        return 'seu time é azul'
    else: 
        return 'seu time é amarelo'



matricula = int(input("Digite um número "))

print(defineTime(matricula))
