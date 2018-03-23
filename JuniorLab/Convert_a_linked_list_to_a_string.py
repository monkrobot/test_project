'''Need to write a function, which returns a string of class Node.data in form: 1 -> 2 -> 8 -> None'''

class Node:
    def __init__(self, data, next='None'):
        self.data = data
        self.next = next

    def return_data(self):
        return self.data



def stringify(seq, n=''):
    if type(seq) == list:
        seq = seq[0]

    seq_num_dot = seq.find(',')
    if seq_num_dot < 0:
        ldict = locals()
        new_seq = 'm = ' + seq
        exec(new_seq)
        exec(
             'n += str(m.data) + " -> " + str(m.next)\n'
             'print("exec n:", n)\n'
             'print("str(m.next)", str(m.next))', ldict)
        n = ldict['n']
        print('n', n)
        answer = n
        print('answer', answer)
        return n
    else:
        ldict = locals()
        new_seq = 'm = ' + seq[:seq_num_dot] + ',' + str([seq[seq_num_dot + 1:][:-1]]) + ')'
        exec(new_seq)
        exec(
             'n += str(m.data) + " -> "\n', ldict)
        m,n = [ldict['m'], ldict['n']]
        return stringify(m.next, n)

print(stringify(' Node(1,  Node(2,  Node(3, Node(5, Node(18, Node(134))))))'))

