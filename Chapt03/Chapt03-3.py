#! /usr/bin/python3.10

from threading import Thread

if __name__ == '__main__':
    thread = Thread()
    # report the thread identifier
    print(thread.native_id)
    # start the thread
    thread.start()
    # report the thread identifier
    print(thread.native_id)