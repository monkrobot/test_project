import numpy as np
import matplotlib.pyplot as plt

#zero_list = np.zeros(5)
#print(zero_list)
##return: [0. 0. 0. 0. 0.]


#error_ = 0
#x = np.arange(10)
#print(np.where(x>3,1,-1))
##return list, where x>3
#for i in np.arange(0,14,0.1):
#    error_ += int(i >= 10)
#    print('i:', i)
#    print(error_)

#x = np.arange(-5, 5, 0.1)
#y = np.arange(-5, 5, 0.1)
#xx, yy = np.meshgrid(x, y, sparse=True)
#print('xx:\n', xx)
#print('yy:\n', yy)
#
#z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
#h = plt.contourf(x,y,z)
#
#plt.show()


##Doesn't work
#def test(new_list):
#    r = np.random.permutation(len(new_list))
#    print('r', r)
#    return new_list[r]
#
#new_list = [x for x in 'python']
#print(test(new_list))

class Node:
    def __init__(self, data, next='None'):
        self.data = data
        self.next = next

    def return_data(self):
        return self.data

seq = ' Node(1,  Node(2,  Node(3, Node(5, Node(18, Node(134))))))'
seq_num_dot = seq.find(',')
new_seq = 'm = ' + seq[:seq_num_dot] + ',' + str([seq[seq_num_dot + 1:][:-1]]) + ')'
exec(new_seq)
print(m.data)