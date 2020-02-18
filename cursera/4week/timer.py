import time
class timer:
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        print('Тек время: {}'.format(time.time() - self.start))

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('Время выполнения: {}'.format(time.time() - self.start))

with timer() as t:
    time.sleep(1)
    t.current_time()
    time.sleep(1)