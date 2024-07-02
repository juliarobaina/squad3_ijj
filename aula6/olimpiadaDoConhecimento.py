def definirGrupo(matricula):
    
    if int(matricula) % 2 == 0:
        return "Grupo Azul"
    else:
        return "Grupo Amarelo"

matricula = input("Digite sua matrícula: ")

while matricula != "sair":
    if int(matricula) < 1:
        print("Matrícula Inválida")
    else:
        print(f"Você está no grupo {definirGrupo(matricula)}")
    matricula = input("Digite sua matrícula: ")

'''
para definir o tipo dos parâmetros a:int
pra definir o tipo do retorno da função -> int
def soma(a:int, b:int) -> int
type hints
'''
