from concurrent.futures import ThreadPoolExecutor
from threading import RLock
from functools import partial # 偏函数

# python创始人写的线程库，最好
lock = RLock()
num = 0
counts = 10000000

# def add(a, b):
def add():
    # print(a)
    # print(b)
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
        # lock.acquire()
        lock.acquire()
        num = num - 1
        # lock.release()
        lock.release()
pools = ThreadPoolExecutor(max_workers=20)  # 最大线程数量

from concurrent.futures import as_completed
function_list = [add, minus]
pools_list = list()
for i in function_list:
    pools_list.append(pools.submit(i))

for i in as_completed(pools_list):
    i.result()


# 因为submit不能接收2个参数传入  如果需要传入两个以上参数要引入partial
# pools.submit(partial(add, 5, 10))
# pools.submit(minus)
print(num)