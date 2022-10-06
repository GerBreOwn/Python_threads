#! /usr/bin/python3.10

from time import sleep
from threading import Thread

class CustomThread(Thread):
    def run(self):
        sleep(1)
        print('This is another thread')

if __name__ == '__main__':
    thread = CustomThread()
    thread.start()
    print('Waiting for thread to finish')
    thread.join()