numerosA = [1,23,24,15,12,24,45,12]
numerosB = [12,-10,-12,23,15, 25]

def numMaior(num):
    maior = 0
    for i in range(len(num)):
        if num[i] > maior:
            maior = num[i]

    print(f'o maior valor é {maior}')
    return maior


numMaior(numerosA)
numMaior(numerosB)
