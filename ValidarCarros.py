carros1 = ["Fusca", "Gol", "Onix", "Corolla", "Civic"]
carros2 = ["HB20", "Uno", "Creta", "Prisma", "Renegade"]
carros3 = ["Mustang", "Camaro", "Challenger", "Corvette", "Ferrari"]


def listarCarros(listaCompleta):
    for i in range(len(listaCompleta)):
        print(listaCompleta[i])


def carroValido(lista):
    validador = False
    listarCarros(lista)

    while validador == False:
        escolha = input('Escolha um dos carros: ')

        for i in range(len(lista)):
            if escolha == lista[i]:
                print('Carro escolhido Existe')
                validador = True
                break


carroValido(carros1)
carroValido(carros2)
carroValido(carros3)
