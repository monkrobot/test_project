'''

'''

s = "chruschtschov"

def solve(s):
    alpha = {}
    for code,numb in zip(range(ord('a'), ord('z')+1), range(1,100)):
        alpha[chr(code)] = numb

    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    letter_weight = 0
    answer = 0
    for i in s:
        if i not in vowel:
            letter_weight += alpha[i]
        else:
            if letter_weight > answer:
                answer = letter_weight
                letter_weight = 0

    return answer

print(solve(s))
