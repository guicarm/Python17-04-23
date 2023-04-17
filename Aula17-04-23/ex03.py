#somar 10 números digitados pelo usuário

# INÍCIO DO LAÇO
soma = 0
for cont in range (1, 10 + 1, 1):

    #DIGITAR 10 NÚMEROS
    n = int(input("Digite o número: "))

    #SOMAR OS NÚMEROS
    soma = soma + n

    #EXIBIR A SOMA DOS NÚMEROS
    print(f"Somatória = {soma}")