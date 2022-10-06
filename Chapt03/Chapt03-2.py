#! /usr/bin/python3.10

from threading import Thread

if __name__ == '__main__':
    # create a thread with a custom name
    thread = Thread(name='MyThread', daemon=True)
    # report thread name
    print(thread.name)
    print(thread.daemon)