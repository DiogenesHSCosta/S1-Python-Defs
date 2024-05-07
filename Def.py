def podeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa, {nome} pode votar")
        return True
    else:
        print(f'Não, a pessoa, {nome} ainda n pode votar')
        return False


a = podeVotar('douglas', 12)
b = podeVotar('Nando', 10)
