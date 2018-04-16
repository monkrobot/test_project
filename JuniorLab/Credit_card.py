n = 4111111111111111

def func(number):
    print(str(number)[0:2])
    if str(number)[0:2] == '34' or '37' and len(str(number)) == 15:
        return("AMEX")
    elif str(number)[0:4] == '6011' and len(str(number)) == 16:
        return ("Discover")
    elif (str(number)[0:2] == '51' or '52' or '53' or '54') and len(str(number)) == 16:
        return ("Mastercard")
    elif str(number)[0] == '4' and len(str(number)) == 16:
        return ("VISA")

print(func(n))
