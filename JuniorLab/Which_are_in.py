a1 = ["live", "arp", "strong"]
#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
a2 = ["lovely", "interesting", "arjpose"]

def strfunc(a1, a2):
    a = sorted(a1)
    answer = []
    for word in a:
        for seq in a2:
            if word in seq:
                answer.append(word)
                break
            else:
                continue
    return answer

print(strfunc(a1,a2))
