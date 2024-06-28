num = int(input("Digite um número: "))

while num != 5:
    num = int(input("Digite um número: "))

for i in range(4):
    print("ainda não chegou a 5")
else:
    print("Chegou a 5")

print("-------------------------------")
for i in range(1,5):
    print("ainda não chegou a 5")
else:
    print("Chegou a 5")

print("-------------------------------")
cont = 0
while cont < 4:
    print("ainda não chegou a 5")
    cont += 1
print("Fim do While")