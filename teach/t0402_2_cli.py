from t0402_2_ser import get
from threading import Thread
import time

now = time.time()

thread_list = list()
for i in range(10):
    i = str(i)
    t = Thread(target=get, args=(i,))
    thread_list.append(t)

for j in thread_list:
    j.start()

for k in thread_list:
    k.join()


duration = time.time() - now

print('下载10次共计耗时:{}秒'.format(duration))