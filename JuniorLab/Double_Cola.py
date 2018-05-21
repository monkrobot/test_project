'''
Шелдон, Леонард, Пенни, Раджеш и Говард стоят в очереди к автомату с газировкой за бутылочкой колы. Первый стоит Шелдон.
Он покупает банку колы, выпивает ее и становится в конец очереди раздвоенный буквально (в конце очереди теперь два Шелдона).
Далее в очереди стоял Леонард, который так же пьет колу и уходит раздвоенным в конец очереди.
Таким образом, если считать, что последняя выпила Пенни и она стояла в очереди третей,
то последовательность будет выглядеть так:
Раджеш, Говард, Шелдон, Шелдон, Леонард, Леонард, Пенни, Пенни
Напишите функцию, которая вернет выпившего колу n-ого человека.

whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1)
"Sheldon"
'''

import time

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = 3667

start = time.time()
def whoIsNext(names,n):
    if len(names) < n:
        for i in range(n//2):
            names.extend([names[i], names[i]])

        return len(names), names[n-1]
    else:
        return len(names), names[n-1]

print(whoIsNext(names,n))
print('time1:', time.time()-start)


#Not good solution
start2 = time.time()

def whoIsNext2(names, n):
    for i in range(n):
        names.extend([names[i], names[i]])
    return len(names), names[n-1]

print(whoIsNext2(names,n))
print('time2:', time.time()-start2)


#Doesn't work
start3 = time.time()

def whoIsNext3(names, n):
    new_names = []
    if len(names) < n:
        for i in names:
            new_names.extend([i,i])
        number = (n - len(names)) % len(new_names)
        return new_names[number-1]
    else:
        return names[n-1]

print(whoIsNext3(names,7230702951))
print('time3:', time.time()-start3)
