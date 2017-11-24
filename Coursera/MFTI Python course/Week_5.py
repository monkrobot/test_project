#import time
#import os
#
#pid = os.getpid()
#
#while True:
#    print(pid, time.time())
#    time.sleep(2)

#import time
#import os
#
#pid = os.fork()
#
#if pid == 0:
#    while True:
#        print("child:", os.getpid())
#        time.sleep(5)
#else:
#    print("parent:", os.getpid())
#    os.wait()

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break

    print(data.decode("utf8"))

conn.close()
sock.close()