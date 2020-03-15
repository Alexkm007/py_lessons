import time
import os
# создание процесса на Phyton
pid = os.fork()

if pid == 0:
    #дочериний процесс
    while True:
        print("child:",os.getpid())
        time.sleep(5)
else:
    #родительский процесс
    print("parent:",os.getpgid())
    os.wait()