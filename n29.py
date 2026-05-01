nome=(str(input("escreva o nome do usuário")))
senha=(str(input("escreva a senha do usuário")))

if nome != "" and senha != "":
    print("Usuário e senha são válidos (não estão vazios).")
else:
    print("Usuário ou senha está vazio.")
