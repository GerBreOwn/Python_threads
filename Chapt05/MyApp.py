#! /usr/bin/python3.10

from time import sleep
from threading import Thread
import threading

w_count = 0
w_gust = 0
w_speed = 0
w_angle = 0
w_dir = None
r_count = 0
rainfall = 0
humidity = 0
pressure = 0
temperature = 0

def wind_spin():
    '''This function will count the number of times the reed switch is closed.'''
    print('wind_spin')
    pass

def wind_speed():
    '''This function will calculate the current wind speed.'''
    print('wind_speed')
    pass

def wind_direction():
    '''This function will calculate the current wind direction.'''
    print('wind_direction')
    pass

def tipped():
    '''This will count the number of times the reed switch is closed when the buckets are tipped.'''
    print('tipped')
    pass

def rainfall():
    '''This function will calculate the amount of rainfall when it is raining.'''
    print('rainfall')
    pass

def bme280():
    '''This function will receive the humidity, pressure and temperature from a BME280 sensor module.'''
    print('bme280')
    pass

def battery():
    '''This function will collect data from the battery to be stored in the database.'''
    print('battery')
    pass

def database():
    '''This function will save the data from the above functions to the PostgreSQL database'''
    print('database')
    pass

if __name__ == '__main__':
    threads = []
    thread_spin = Thread(target=wind_spin, name='wind_spin')
    thread_speed = Thread(target=wind_speed, name='wind_speed')
    thread_direction = Thread(target=wind_direction, name='wind_direction')
    thread_tipped = Thread(target=tipped, name='tipped')
    thread_rainfall = Thread(target=rainfall, name='rainfall')
    thread_bme280 = Thread(target=bme280, name='bme280')
    thread_battery = Thread(target=battery, name='battery')

    threads = [thread_spin, thread_speed, thread_direction, thread_tipped,thread_rainfall, thread_bme280,  thread_battery]

    for thread in threads:
        thread.start()
    running_threads = threading.enumerate()
    print(f'Active Threads: {len(running_threads)}')
    # report each in turn
    for thread in running_threads:
        print(thread)