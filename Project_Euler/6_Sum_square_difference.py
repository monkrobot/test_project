'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

N = 100
summa = 0
sum_of_sqrs = 0

for i in range(1, 101):
    summa += i
    sum_of_sqrs += i**2

sqr_of_summa = summa**2

print("answer", sum_of_sqrs - sqr_of_summa)