'''
Напишите функцию, которая принимает строку скобок.
Нужно определить, является ли валидной последовательность скобок.
Если последовательность валидна, вернуть true, иначе - false.
Все строки не пустые и будут состоять из следующих скобок: (){}[]
'''
braces = "(})"

def validbraces(braces):
    open_brac = ['(', '{', '[']
    close_brac = [')', '}', ']']
    sequence = []
    #if braces[0] in close_brac:
    #    return False
    for i in braces:
        if i in open_brac:
            sequence.append(i)
        if i in close_brac:
            try:
                if i == close_brac[open_brac.index(sequence[-1])]:
                    sequence.pop()
                    continue
                else:
                    return False
            except:
                return False
            #else:
            #    return False
    if sequence == []:
        return True
    else:
        return False

print(validbraces(braces))
