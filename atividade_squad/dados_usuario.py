nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

somando_notas = nota1 + nota2

#print(type(idade))  Apenas para verificar o tipo de dado
#print(type(altura))  Apenas para verificar o tipo de dado

print(f"O nome do usuario é {nome}, sua altura em metros é {altura}, e sua idade é {idade} anos.")
print(f"A soma das duas notas é {somando_notas}")