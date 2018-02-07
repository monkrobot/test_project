import numpy as np

f = np.arange(0, 24, 2).reshape((3, 4))


print('f\n', f)
print(f[[2, 1], [0, 2]])
print('f.T\n', f.T)