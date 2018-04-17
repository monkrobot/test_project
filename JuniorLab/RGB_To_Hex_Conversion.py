n = 15
print(str(hex(n)))
print(int('ff', 16))

def rgb(red, green, blue):
    result = ''
    for i in [red, green, blue]:
        if i < 16:
            color = '0' + str(hex(i))[2:]
        else:
            color = str(hex(i))[2:]
        result += color.upper()
    return result

print(rgb(255, 11, 211))