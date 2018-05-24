'''
n is a number of floors
Need to build a house as follows:
        ___
       /___\
      /_____\
      |  _  |  // 1 floor
      |_|_|_|

       _____
      /_____\
     /_______\
    /_________\
   /___________\
   |           |
   |    ___    |  // 2 floors
   |   |   |   |
   |___|___|___|
'''

n = 3

def my_crib(n):
    ans = [[], [], [], []] #[top_line, roof, space, door]
    ans[0].append('{0}{1}{0}\n'.format(2*n* ' ', (n * 2 + 1) * '_'))

    for i in range(1, n+1):
        ans[1].append('{0}/{1}\\{0}\n'.format((2*(n-i)+1)*' ', ((2*n + 1) + 4*(i-1))*'_'))
        ans[1].append('{0}/{1}\\{0}\n'.format((2*(n-i))*' ', ((n * 2 + 3) + 4*(i-1))*'_'))
        if n == 1:
            ans[3].append('|{0}{1}{0}|\n'.format((n * 2) * ' ', (n+n-1)*'_'))
        elif ans[3] == []:
            ans[3].append('|{0}{1}{0}|\n'.format((n * 2) * ' ', (n + n - 1) * '_'))
        elif i > 1:
            ans[2].append('|%s|\n' % ((6*n - 1)*' '))
            ans[3].append('|{0}|{0}|{0}|\n'.format((2*n-1)*' '))
        if i == n:
            ans[3].append('|{0}|{0}|{0}|'.format((2 * n - 1) * '_'))

    answer = []
    for i in ans:
        answer.extend(i)
    return ''.join(answer)



print(my_crib(n))

