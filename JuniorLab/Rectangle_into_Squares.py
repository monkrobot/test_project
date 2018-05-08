lng = 16
width = 3

def func(lng, width):
    answer = []
    #if lng == width:
    #    return "null"
    #elif lng > width:

    #Try to make lng > width
    if lng < width:
        cap = lng
        lng = width
        width = cap

    while
    answer.append(width)
    lng = lng - width
    return func(lng, width)
    else:
        answer.append((width-lng))
