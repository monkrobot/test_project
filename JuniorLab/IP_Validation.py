str = " 1.2.3.4"

def isvaliip(str):
    try:
        ip = [int(x) for x in str.split('.') if ' ' not in x]
    except:
        return False
    if len(ip) < 4:
        return False
    for i in ip:
        if i in range(256):
            continue
        else:
            return False
    return True

print(isvaliip(str))
