#import my

def countLines(name):
    f = open(name)
    return len(f.readlines())

def countChars(name):
    f = open(name)
    return len(f.read())

def test(name):
    print("test\n")
    print(countLines(name))
    print(countChars(name))


#print(countLines('my.py'))
#print(countChars('my.py'))
if __name__ != '__main__':
    print("\nif\n")
    print(test('my.py'))