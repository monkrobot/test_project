import mypkg.mymod
import imp

print(mypkg.mymod.countLines('my.py'))
print(mypkg.mymod.countChars('my.py'))
print('reload')
imp.reload(mypkg.mymod)
print('after reload')
print(mypkg.mymod.test('my.py'))
