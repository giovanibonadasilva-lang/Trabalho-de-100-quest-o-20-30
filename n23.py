a = int(input("Digite o primeiro valor (0 ou 1): "))
b = int(input("Digite o segundo valor (0 ou 1): "))
abl=bool
bbl=bool
if a == 1 and b == 1:
    print("AND: verdadeiro")
else:
    print("AND: falso")

if a == 1 or b == 1:
    print("OR: falso")
else:
    print("OR: verdadeiro")

if a == 1:
    print("NOT A: falso")
else:
    print("NOT A: verdadeiro")

if b == 1:
    print("NOT B: falso")
else:
    print("NOT B: verdadeiro")