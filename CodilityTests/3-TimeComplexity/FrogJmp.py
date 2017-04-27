#What is the min number of jumps, which length is D, to achieve position Y from position X
#100%
import math
def solution(X,Y,D):

    jumpes = math.fabs(Y - X) / D
    return math.ceil(jumpes)

#def solution(X, Y, D):
#    if (Y-X) / D > (Y - X) // D:
#        jumpes = (Y - X) // D + 1
#    else:
#        jumpes = (Y - X) // D
#    return jumpes

print(solution(10, 85, 30))