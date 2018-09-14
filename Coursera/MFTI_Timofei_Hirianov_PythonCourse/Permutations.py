#def generate_number(N:int, M:int, prefix=None):
#    prefix = prefix or []
#    if M == 0:
#        print(prefix)
#        return
#
#    for i in range(N):
#        #print("prefix: ", prefix)
#        prefix.append(i)
#        generate_number(N, M-1, prefix)
#        prefix.pop()
#
#
#generate_number(4,4)


def generate_number(N:int, M:int=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for i in range(1, N+1):
        if i in prefix:
            continue
        prefix.append(i)
        generate_number(N, M-1, prefix)
        prefix.pop()


generate_number(5,5)
