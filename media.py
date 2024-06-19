'''n1 = float(input("Digite nota 1: "))
n2 = float(input("Digite nota 2: "))
n3 = float(input("Digite nota 3: "))
n4 = float(input("Digite nota 4: "))

result = (n1+n2+n3+n4) / 4

print(f"media e {result:.2f}")
'''
soma = 0
for i in range(0,4):
    soma += float(input(f"Digite sua {i+1}ª nota: "))

media = soma / (i + 1)
print(f"media e {media:.2f}")

