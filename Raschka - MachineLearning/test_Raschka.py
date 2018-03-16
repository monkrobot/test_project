import numpy as np
import matplotlib.pyplot as plt
#error_ = 0
#x = np.arange(10)
#print(np.where(x>3,1,-1))
#for i in np.arange(0,14,0.1):
#    error_ += int(i >= 10)
#    print('i:', i)
#    print(error_)

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
print('xx:\n', xx)
print('yy:\n', yy)

z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)

plt.show()