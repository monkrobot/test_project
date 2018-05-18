'''
About Pascal's Triangle: http://en.wikipedia.org/wiki/Pascal's_triangle
Write a function, which takes depth of triangle and returns one-dimensional array of Pascal's triangle
'''

n=5

def pascalstriangle(n):
    row = []
    answer = []
    for i in range(1, n+1):
        row.append([None] * i)
        print(row)
        if i == 1:
            answer.append(1)
            row[0][0] = 1
        elif i == 2:
            row[i-1] = [1] * 2
            answer.extend(row[i-1])
        else:
            row[i-1][0] = row[i-1][-1] = 1
            for j in range(1, i-1):
                row[i-1][j] = row[i-2][j-1] + row[i-2][j]
            answer.extend(row[i-1])
    return answer

print(pascalstriangle(n))
