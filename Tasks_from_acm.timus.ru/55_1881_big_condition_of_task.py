h = 3
w = 5
n = 6


words = ['to', 'be', 'or', 'not', 'to', 'be']

def testing(words):
    string = 0
    count = 0
    for i in range(0, len(words)):
        if len(words[i]) > w:
            print('Error! This word: ' + str(words[i]) + ' - is too big')
        else:
            if count + len(words[i]) <= w:
                count += len(words[i]) + 1
                print("if. Count i = " + str(i) + " = " + str(count))
            else:
                string += 1
                count = len(words[i]) + 1
                print("else. Count i = " + str(i) + " = " + str(count))
                print("else. string i = " + str(i) + " = " + str(string))
    string += 1
    print(string)

testing(words)