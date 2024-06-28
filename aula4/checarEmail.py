num = int(input("Digite o número de usuários: "))
emails = []

for i in range(num):
    emails.append(input(f"Digite o e-mail do {i+1}º usuário: "))

for email in emails:
    emailSplit = email.split('@')
    if len(emailSplit) == 2:
        if ("jogajuntoinstituto.org" not in emailSplit[1]) or emailSplit[0] == "":
            print(f"\nO {email} é inválido")
    else:
        print(f"\nO {email} é inválido")

    

