def validaNumero(num):
    while not num.isnumeric():
        print(type(num))
        num = input("insira um numero valido: ")

    return num

def validarTelefone(tel):

    tel = validaNumero(tel)

    if len(tel) > 11 or len(tel) < 9:
        print('numero invalido')
        return False
    else:
        print('Numero valido')
        return True


print(validarTelefone('adfa'))

