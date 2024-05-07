def idade(nome, idade):
    idade = 2024 - idade
    print(f'idade do(a) {nome} é {idade}')
    return idade


pessoa = idade('douglas', 2004)

print(pessoa)
