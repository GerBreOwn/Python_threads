#! /usr/bin/python3.10

from time import sleep
from threading import Thread
import threading

def wind_speed():
    '''This function will calculate the current wind speed.'''
    print('wind_speed')
    pass

def wind_direction():
    '''This function will calculate the current wind direction.'''
    print('wind_direction')
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

if __name__ == '__main__':
    thread_speed = Thread(target=wind_speed, name='wind_speed')
    thread_direction = Thread(target=wind_direction, name='wind_direction')
    thread_rainfall = Thread(target=rainfall, name='rainfall')
    thread_bme280 = Thread(target=bme280, name='bme280')
    thread_battery = Thread(target=battery, name='battery')

    print(thread_battery.name)
    print(thread_bme280.name)
    print(thread_direction.name)
    print(thread_speed.name)  
    print(thread_rainfall.name)

    """ thread_speed.start()
    thread_direction.start()
    thread_rainfall.start()
    thread_bme280.start()
    thread_battery.start() """
    for thread in threads:
        thread.start()
    running_threads = threading.enumerate()
    print(f'Active Threads: {len(running_threads)}')
    # report each in turn
    for thread in running_threads:
        print(thread)