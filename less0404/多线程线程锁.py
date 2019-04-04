from threading import Thread
from threading import Lock,RLock
num = 0
counts = 10000000
# lock = Lock()
lock = RLock()
def add():
    global num
    global counts
    # num = 0
    # counts = 10000000
    for i in range(counts):
        lock.acquire()
        num = num + 1
        lock.release()

def minus():
    global num
    global counts
    # num = 0
    # counts = 10000000
    for i in range(counts):
        lock.acquire()
        lock.acquire()
        num = num - 1
        lock.release()
        lock.release()

# add()
# minus()
# print(num)
t1 = Thread(target=add)
t2 = Thread(target=minus)
t1.start()
t2.start()
t1.join()
t2.join()
print(num)