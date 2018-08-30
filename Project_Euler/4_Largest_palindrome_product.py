'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

n = 3

number1 = int('9' + '9'*(n-1))
number2 = int('9' + '9'*(n-1))
stop_num = int('1' + '0'*(n-1))
palindromic = 0
flag = 0

for i in range(number1, stop_num, -1):
    if flag >= 3:
        break
    for j in range(number1, stop_num, -1):
        print('1:', i)
        print('2:', j)
        ij = i * j
        print(ij, str(ij), ''.join(list(reversed(str(ij)))))
        if ij < palindromic:
            flag += 1
            break
        elif str(ij) == ''.join(list(reversed(str(ij)))):
            if ij > palindromic:
                palindromic = ij
                flag -= 1
                break
            else:
                break
        else:
            continue
    else:
        flag -=1

print(palindromic)
print('flag:', flag)
