rows = 9
for i in range(1, rows + 1):
    # Adiciona espaços para alinhar à direita, criando o formato invertido
    print(" " * (rows - i) * 2, end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
input()
