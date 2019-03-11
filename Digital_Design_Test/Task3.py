'''
Sort two large files (50 points). You have two files a.txt and b.txt in your working
directory. Write a program that creates file c.txt containing all lines from a.txt and b.txt in
lexicographical order.
(Be aware that both files a.txt and b.txt can be large than available RAM).
For example:
Input:

a.txt
yyy
sss
iii
👍👍👍

b.txt
uuu
aaa
ddd
👌👌👌

c.txt:
aaa
ddd
iii
sss
uuu
yyy
👌👌👌
👍👍👍
'''


# Doesn't work with huge files
with open("a.txt", "r") as a, open("b.txt", "r") as b, open("c.txt", "w") as c:
    file_list = []
    for line in a:
        file_list.append(line.rstrip())
    for line in b:
        file_list.append(line.rstrip())
    file_list.sort()
    text = '\n'.join(file_list)
    c.write(text)





#import pandas as pd
## Doesn't work with huge files
#with open("2008.txt", "r") as a, open("b.txt", "r") as b, open("c.txt", "w") as c:
#    k = pd.read_csv("a.txt")
#    #print(df)
#    #list_a = list(a)
#    #list_a[-1] = list_a[-1] + '\n'
#    #list_b = list(b)
#    #list_b[-1] = list_b[-1] + '\n'
#    #file_list = list_a + list_b
#    #file_list.sort()
#    #print(file_list)
#    #text = ''.join(file_list)
#    k.sort([0])
#    k.to_csv("c2.txt")