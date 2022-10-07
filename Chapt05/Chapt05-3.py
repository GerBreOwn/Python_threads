#! /usr/bin/python3.10

from time import sleep
from threading import Thread
from queue import Queue

def task(shared_queue):
    sleep(1)
    # prepare some data
    item = 'Hello from a new thread'
    shared_queue.put(item)

if __name__ == '__main__':
    queue = Queue()
    thread = Thread(target=task, args=(queue,))
    thread.start()
    data = queue.get()
    print(data)