import threading

class FM(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = FM(name='send out pesant')
y = FM(name='menerima')
x.start()
y.start()