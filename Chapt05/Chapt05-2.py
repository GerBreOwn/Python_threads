#! /usr/bin/python3.10

from time import sleep
from threading import Thread

class CustomThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.value = None
    def run(self):
        sleep(1)
        self.value = 'Hello from a new thread'

if __name__ == '__main__':
    thread = CustomThread()
    thread.start()
    thread.join()
    data = thread.value
    print(data)