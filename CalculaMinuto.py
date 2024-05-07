
def proximoMinuto(hora, min):
    if hora >23 or min >59:
        return 'Insira uma hora valida'
    elif min != 59:
        return f'{hora}:{min+1}'

    elif hora == 23 and min == 59:
        return f'0{0}:0{0}'

    elif hora != 23 and min == 59:
        return f'{hora+1}:0{0}'

print(proximoMinuto(22,59))


