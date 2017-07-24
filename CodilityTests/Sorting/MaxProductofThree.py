A = [-3, 1, 2, -2, 5, 6]

#100%
B = sorted(A)
print(B)
print('Negative: ', B[0]*B[1]*B[-1])
print('Positive: ', B[-1]*B[-2]*B[-3])
if B[0]*B[1]*B[-1] > B[-1]*B[-2]*B[-3]:
    maxprod = B[0] * B[1] * B[-1]
else:
    maxprod = B[-1] * B[-2] * B[-3]

print(maxprod)

