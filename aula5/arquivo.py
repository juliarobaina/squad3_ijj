userChoice = int(input('Escolha 1 para ler ou 2 para escrever no arquivo: '))

match userChoice:
    case 1:
        with open('timesShinobis.txt','r') as file:
            print(file.read())
    case 2:
        print('-> ', end='')
        data = input('')
        with open('timesShinobis.txt','a') as file:
            file.write(data + '\n')
    case _:
        print('opção inválida, tente novamente')
