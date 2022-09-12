from maquina import Estados

e1 = Estados()

usuario = -1

while usuario != 0:
    print("-"*10)
    usuario = int(input("Digite:"
                        "\n1 - Verificar transições possíveis"
                        "\n2 - Alterar transição"
                        "\n3 - Alterar estado"
                        "\n4 - Mostrar status"
                        "\n0 - Para encerrar"
                        "\nEntrada: "))

    if usuario == 1:
        e1.verificarTransicao()
    if usuario == 2:
        e1.alterarTransicao(input("Digite a transição: "))
    if usuario == 3:
        e1 = Estados(input("Digite o estado: "))
    if usuario == 4:
        e1.imprimeStatus()