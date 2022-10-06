#! /usr/bin/python3.10

from concurrent.futures import thread
from time import sleep
from threading import Thread
from threading import local

def task(shared_local):
    sleep(1)
    shared_local.value = 33
    print(f'Thread stored: {shared_local.value}')

if __name__ == '__main__':
    local_storage = local()
    local_storage.value = 100
    print(f'Main stored: {local_storage.value}')
    thread = Thread(target=task, args=(local_storage,))
    thread.start()
    thread.join()
    print(f'Main sees: {local_storage.value}')
