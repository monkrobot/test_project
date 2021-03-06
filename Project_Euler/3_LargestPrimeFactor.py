'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt
n = 600851475143

factors = []
#Находим все делители без остатка для числа n и записываем их в factors
for i in range(2, int(sqrt(n))):
    if n%i == 0:
        factors.extend([i,n//i])
#Ищем делители у чисел из factors
for j in reversed(sorted(factors)): #сортируем factors от меньшего к большему, а затем переворачиваем список
    for k in range(2,int(sqrt(j))):
        if j%k == 0:
            print('{0} break on {1}'.format(j,k))
            break
    else: #если цикл закончился самостоятельно, а не на break, т.е. делителей не нашлось
        print("answer is: ", j)
        break

print("factors of n: ", list(reversed(sorted(factors))))



#num = 600851475143
#
##берем корень из числа, поскольку он не целый, округляем до целого
#sqr = round(num**0.5)
#
#def isPrime(n):
#    for i in range(2,int(n**0.5)+1):
#        if n%i==0:
#            return False
#    return True
#
#
#for i in range(sqr+1,2,-2): #пробегаем по всем нечетным числам от нашего корня в обратном порядке
#    if num%i == 0:
#        if isPrime(i): #останавливаемся на первом простом. Это и есть искомое число
#            print(i)
#            break
#