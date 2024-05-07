
def podeVotar(nome, idade):
    idade = calculaIdade(idade)
    if idade >= 16:
        print(f"Sim, a pessoa, {nome} pode votar")
        return True
    else:
        print(f'Não, a pessoa, {nome} ainda n pode votar')
        return False
def calculaIdade(ano):
    idade = 2024 - ano
    return idade


pessoa = podeVotar('douglas', 2004)

print(pessoa)
