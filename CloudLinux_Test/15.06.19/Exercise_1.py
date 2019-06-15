A = [0,1]


def solution(ar):
    valley = 0
    hill = 0

    castles = 0

    flag = 0

    for i in range(len(ar)-1):
        # if ar[i] < 0:
        #     return "negative number"
        if ar[i] == ar[i+1]:
            continue
        elif ar[i] > ar[i+1] and flag <= 0:
            hill += 1
            castles += 1
            flag = 1
            print('hill: ', hill)
        elif ar[i] < ar[i+1] and flag >= 0:
            flag = -1
            # if ar[i]:
            valley += 1
            castles += 1
            print('valley: ', valley)

    # if ar[-1] < 0:
    #     return "Negative number"
    # elif ar[-1]:
    castles += 1

    return castles


#     p = len(ar) // 2
#     q = len(ar) - p
#     for i in range(1, p+1):
#         if ar[i] == ar[i - 1]:
#             continue
#         elif ar[i - 1] < ar[i] and flag <= 0:
#             hill += 1
#             castles += 1
#             flag = 1
#             print('hill: ', hill)
#         elif ar[i] < ar[i - 1] and flag >= 0:
#             flag = -1
#             valley += 1
#             castles += 1
#             print('valley: ', valley)
#
#     for j in range(len(ar)-p, len(ar)):
#         if ar[i] == ar[i - 1]:
#             continue
#         elif ar[i + 1] < ar[i] and flag <= 0:
#             hill += 1
#             castles += 1
#             flag = 1
#             print('hill: ', hill)
#         elif ar[i] < ar[i + 1] and flag >= 0:
#             flag = -1
#             valley += 1
#             castles += 1
#             print('valley: ', valley)
#
#     castles += 1
#     return castles


if __name__ == "__main__":
    print(solution(A))
