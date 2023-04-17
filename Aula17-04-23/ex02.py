while True:
    vi = int(input("Digite o valor inicial: "))
    vf = int(input("Digite o valor final: "))

    while vi <= vf:
        print(vi)
        vi = vi + 1

    opcao = input("Continuar? [S/N]: ")
    if opcao == 'n' or opcao == 'N':
        break
