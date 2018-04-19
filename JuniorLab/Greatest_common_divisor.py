import time

n = 1590771464
m = 1590771620

start = time.time()

#It works, but too slow
def func(n,m):
    if n > m:
        max_num = n
        min_num = m
    else:
        max_num = m
        min_num = n
    for i in range(1,min_num+1):
        if min_num % i == 0:
            max_dev = min_num / i
            if max_num % max_dev == 0:
                return int(max_dev)
        else:
            continue

print(func(n,m))

print(time.time()-start )