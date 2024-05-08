def proximoMinuto(hora, min):
    if hora > 23 or min > 59:
        return 'Insira uma hora valida'

    elif min != 59:
        return f'{hora}:{min + 1}'

    elif hora == 23 and min == 59:
        return f'00:00'

    elif hora != 23 and min == 59:
        return f'{hora + 1}:0{0}'


print(proximoMinuto(22, 59))
print(proximoMinuto(1, 23))
print(proximoMinuto(12, 2))
print(proximoMinuto(20, 59))
