#! /usr/bin/python3.10

from threading import Thread
from threading import current_thread
from threading import main_thread

if __name__ == '__main__':
    # get the current thread
    # thread = current_thread()
    thread = main_thread()
    # report details
    print(thread)