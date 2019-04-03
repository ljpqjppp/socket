import time
from threading import Thread


def test1(a, b):
    time.sleep(5)
    print('test1 end{} {}'.format(a, b))


def test2():
    time.sleep(2)
    print('test2 end')


t1 = Thread(target=test1, args=(5, 6))
t1.start()
test2()
