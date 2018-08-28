'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

N = 4000000
b = 1
j = 0
answer = 0
numbers = []

while b <= N:
    if b % 2 == 0:
        answer += b
    numbers.append(b)
    m = b
    b += j
    j = m

print('answer:', answer)
print('numbers:', numbers)