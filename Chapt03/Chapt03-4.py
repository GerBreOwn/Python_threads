#! /usr/bin/python3.10

from threading import Thread

if __name__ == '__main__':
    thread = Thread()
    print(thread.is_alive())
    thread.start()
    print(thread.is_alive())