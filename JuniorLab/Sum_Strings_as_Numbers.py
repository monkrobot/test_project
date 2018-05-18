'''
Write a function, which takes 2 str args - numbers and returns str sum of this numbers
'''

a = "712569312664357328695151392"
b = "8100824045303269669937"

def sumstrings(a, b):
    return str(int(a) + int(b))

true_ans = "712577413488402631964821329"
ans = sumstrings(a,b)
print(sumstrings(a,b))
if ans == true_ans:
    print(True)
