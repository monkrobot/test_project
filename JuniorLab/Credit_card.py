import time

n = 5205105105105106

start1 = time.time()

def func(number):
    if str(number)[0:2] == '34' or str(number)[0:2] == '37' and len(str(number)) == 15:
        return "AMEX"
    elif str(number)[0:4] == '6011' and len(str(number)) == 16:
        return "Discover"
    elif str(number)[0:2] == '51' or str(number)[0:2] == '52' or str(number)[0:2] == '53' \
            or str(number)[0:2] == '54' and len(str(number)) == 16:
        return "Mastercard"
    elif str(number)[0] == '4' and len(str(number)) == 16 or len(str(number)) == 13:
        return "VISA"
    else:
        return "Unknown"

print(func(n))

print('time1:', time.time() - start1)

#Not good solution
start2 = time.time()

def func2(number):
    if len(str(number)) == 15 and str(number)[0:2] == '34' or str(number)[0:2] == '37':
        return "AMEX"
    if len(str(number)) == 13 and str(number)[0] == '4':
        return "VISA"
    if len(str(number)) == 16:
        if str(number)[0] == '4':
            return "VISA"
        elif str(number)[0:2] == '51' or str(number)[0:2] == '52' or str(number)[0:2] == '53' \
                or str(number)[0:2] == '54' or str(number)[0:2] == '55':
            return "Mastercard"
        elif str(number)[0:4] == '6011':
            return "Discover"
        else:
            return "Unknown"
    else:
        return "Unknown"

print(func2(n))
print(start2)
final = time.time()
print(final)
print('time2:', time.time() - start2)
