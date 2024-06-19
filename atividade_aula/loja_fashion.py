valor_compra = float(input("Digite o valor total da sua compra: R$ "))

if valor_compra > 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
    desconto = valor_compra - (valor_compra * 0.30)
    print(f"O valor da sua compra é: {desconto:.2f}")
elif valor_compra >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
    desconto = valor_compra - (valor_compra * 0.10)
    print(f"O valor da sua compra é: {desconto:.2f}")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")


