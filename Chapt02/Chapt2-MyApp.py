#! /usr/bin/python3.10

from time import sleep
from threading import Thread
from gpiozero import Button

w_sensor = Button(5)

def speed():
    global w_count
	w_count += 1

def direction():
    pass


if __name__ == '__main__':
    thread_speed = Thread(target=speed)
    thread_direction = Thread(target=direction)
    w_sensor.when_pressed = thread_speed.start