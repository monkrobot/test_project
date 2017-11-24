## Пул потоков, concurrent.futures.Future
#
#from concurrent.futures import ThreadPoolExecutor, as_completed
#
#def f(a):
#    return a * a
#
## .shutdown() in exit
#with ThreadPoolExecutor(max_workers=3) as pool:
#    results = [pool.submit(f, i) for i in range(10)]
#
#    for future in as_completed(results):
#        print(future.result())


## Синхронизация потоков, блокировки
#
#import threading
#
#
#a = threading.RLock()
#b = threading.RLock()
#
#def foo():
#    try:
#        a.acquire()
#        b.acquire()
#    finally:
#        a.release()
#        b.release()


## Синхронизация потоков, условные переменные
#
#class Queue(object):
#    def __init__(self, size=5):
#        self._size = size
#        self._queue = []
#        self._mutex = threading.RLock()
#        self._empty = threading.Condition(self._mutex)
#        self._full = threading.Condition(self._mutex)
#
#    def put(self, val):
#        with self._full:
#            while len(self._queue) >= self._size:
#                self._full.wait()
#
#            self._queue.append(val)
#            self._empty.notify()
#
#    def get(self):
#        with self._empty:
#            while len(self._queue) == 0:
#                self._empty.wait()
#
#            ret = self._queue.pop(0)
#            self._full.notify()
#            return ret