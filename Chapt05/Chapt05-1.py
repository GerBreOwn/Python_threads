#! /usr/bin/python3.10

from time import sleep
from threading import Thread

def task():
    sleep(1)
    global data
    data = 'Hello from a new thread'

if __name__ == '__main__':
    data = None
    thread = Thread(target=task)
    thread.start()
    thread.join()
    print(data)