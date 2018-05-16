'''
Напишите алгоритм, который будет проверять, являются ли IPv4 адреса валидными.
IP-адреса валидны, если они состоят из 4 октетов со значениями между 0..255 (включительно)
Входной аргумент является строкой с IP адресом.
'''

str = " 1.2.3.4"

def isvaliip(str):
    try:
        ip = [int(x) for x in str.split('.') if ' ' not in x]
    except:
        return False
    if len(ip) < 4:
        return False
    for i in ip:
        if i < 256 and i > 0:
            continue
        else:
            return False
    return True

print(isvaliip(str))
