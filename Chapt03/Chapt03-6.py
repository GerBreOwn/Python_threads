#! /usr/bin/python3.10

from time import sleep
from threading import Thread
import threading

def task():
    sleep(1)

if __name__ == '__main__':
    threads = [Thread(target=task) for _ in range(25)]
    for thread in threads:
        thread.start()
        running_threads = threading.enumerate()
        print(f'Active Threads: {len(running_threads)}')
    for thread in running_threads:
        print(thread)