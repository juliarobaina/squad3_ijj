def verificar_matricula(numero_matricula):
    if numero_matricula % 2 == 0:
        print(f"Número de matrícula {numero_matricula}: VOCÊ ESTÁ NO TIME AZUL")
    else:
        print(f"Número de matrícula {numero_matricula}: VOCÊ ESTÁ NO TIME AMARELO")


def main():
    lista_matriculas = [] 

    print("Por favor, insira até 5 números de matrícula.")

    while len(lista_matriculas) < 5: 
        try: 
            numero = int(input(f"Digite o número da matrícula {len(lista_matriculas)+1}:"))
            lista_matriculas.append(numero) 
        except ValueError:  
            print("Por favor, insira um número válido")
    print("\nVerificando os grupos dos números de matrícula inseridos...\n")


    for numero in lista_matriculas: 
        verificar_matricula(numero) 

if __name__ == "__main__":  
 main() 