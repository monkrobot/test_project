'''
Task 1. Downsampling (10 points). Write a program that decreases sampling frequency of an
array M by some integer factor n.
For example:
Input:
M = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
Output:
M = [1, 3, 5, 7]
Input:
M = [[11 12 13 14 15 16]
[21 22 23 24 25 26]
[31 32 33 34 35 36]
[41 42 43 44 45 46]
[51 52 53 54 55 56]
[61 62 63 64 65 66]]
n = 2
Output:
[[11 13 15]
[31 33 35]
[51 53 55]]
'''


def downsampling(m, n):
    '''
    Func decreases sampling frequency of an array M by some integer factor n.
    :param m: array
    :param n: integer factor
    :return:
    '''

    if not isinstance(m, list):
        print('M need to be an array')
    else:
        answer = []
        for i in range(0, len(m), n):
            if isinstance(m[i], list):
                downsampling(m[i], n)
            else:
                if m[i]: # don't work correct
                    answer.append(m[i])
                else: continue

        print(answer)


if __name__ == "__main__":
    M = [[11, 12, 13, 14, 15, 16],
         [21, 22, 23, 24, 25, 26],
         [31, 32, 33, 34, 35, 36],
         [41, 42, 43, 44, 45, 46],
         [51, 52, 53, 54, 55, 56],
         [61, 62, 63, 64, 65, 66]]
    n = 2
    downsampling(M, n)

