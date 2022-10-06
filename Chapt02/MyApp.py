#! /usr/bin/python3.10

from time import sleep
from threading import Thread

def speed():
    '''This function will calculate the current wind speed.'''
    pass

def direction():
    '''This function will calculate the current wind direction.'''
    pass

if __name__ == '__main__':
    thread_speed = Thread(target=speed)
    thread_direction = Thread(target=direction)
