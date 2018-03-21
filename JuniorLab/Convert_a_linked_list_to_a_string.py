class Node:
    def __init__(self, data, next='null'):
        self.data = data
        self.next = next

    def return_data(self):
        return self.data
n = ''

#Return error because m.data = number, but m.next is a class (__main__Node object...)
def stringify(seq):
    new_seq = 'm = Node(0, ' + seq + ')'
    exec(new_seq)
    exec('global n\n'

         'n += str(m.next.data) + " ->"\n'
         'i = 1\n'
         'stringify(str(m.next))')
         #'while i < number:\n'
         #'  k = m.next\n'
         #'  n += str(k.data) + " ->"\n'
         #'  i += 1')
    #exec('while m.next != "null":'
    #     'print(m.next)')


stringify('Node(1, Node(2, Node(3)))')
print(n)


m = Node(5, Node(6))
print('data:', m.data)
print('next:', m.next.next)
