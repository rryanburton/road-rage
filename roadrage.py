import random
# %matplotlib inline  #for ipython notebook graphing
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import math

class Car():
    '''
    Responsibilities:
    - set max speed
    - define vehicle size
    - keep track of velocity
    - keep track of position
    - deal with acceleration or slowing
    - maintain minimum spacing with car in front

    '''
    def __init__(self, position = 0, speed = 15, max_v = 33, length = 5):
        self.max_v = max_v # m/s
        self.length = length # m
        self.current_v = speed
        self.pos = position #spot between 0-1000

        self.spacing = self.current_v

    def __str__(self):
        return 'Car(position={},current_v={})'.format(
                self.pos,  self.current_v)

    def __repr__(self):
        return self.__str__()
    # def set_accel(self):
    #     if random.random() <= .1:
    #         self.current_v -= 2
    #         if self.current_v < 0:
    #             self.current_v = 0
    #         else:
    #             return self.current_v
    #     else:
    #         self.current_v += 2
    #         if self.current_v > self.max_v:
    #             self.current_v = self.max_v
    #         else:
    #             return self.current_v

    def movement(self):
        self.pos += self.current_v
        if self.pos > 1000:
            self.pos = (self.pos % 1000)
        return self.pos

    def info_status():
        print(n, self.pos, self.current_v,
              "(count, current position, current_v)")



    # def drive_time(self, timelimit):
    #         n=1
    #         while n < timelimit:
    #             self.set_accel()
    #             self.movement()
    #             print('------------')
    #             print(n, self.pos, self.current_v,
    #                   "(count, current position, current_v)")
    #             n += 1

class Road():
    '''
    Responsibilities:
    - have cars
    - set number of cars
    - set length of track
    -moving cars


    Collaborate:
    -Car class

    '''
    def __init__(self, num_of_cars = 30):
        self.cars = [Car() for x in range(num_of_cars)]
        self.road_display = np.array([0 for x in range(1000)])

    def __str__(self):
        return 'Road(cars={})'.format(
                self.cars)

    def __repr__(self):
        return self.__str__()
    def initial_pos(self):
        for car in self.cars:
            car.pos += 33

    def set_accel(self):
        if random.random() <= .1:
            car.current_v -= 2
            if car.current_v < 0:
                car.current_v = 0
            else:
                return car.current_v
        else:
            car.current_v += 2
            if car.current_v > car.max_v:
                car.current_v = car.max_v
            else:
                return car.current_v

    def drives(self):
       return [car.movement() for car in self.cars]

    def update_road_display(self):
        self.road_display = np.array([0 for _ in range(1000)]) #resets the map to 000
        for car in self.cars:  # puts a 1 in all the car spaces
            for x in range(5):
                self.road_display[car.pos+x] = 1

    def check_cars(self):
        return [car.current_v for car in self.cars]

class Simulator():
    '''
    Responsibilities:
    - handles time (ticks)
    - handles moving cars
    - handles data

    '''

    def __init__(self):
        self.ticks = 0
        self.road = Road()

    def tick(self):
        current_v = self.road.check_cars()
        self.road.set_accel()
        self.road.drives()
        self.road.update_road_display()


    def timed_run(self, timelimit = 60):
        self.road.initial_pos()
        for sec in range(timelimit):
            self.ticks += 1



# get your data in an np.array, make sure the type is float32 using .astype('float32')

# img_data = np.random.choice([0,1,1], (60, 1000)).astype('float32')
# print(img_data)
#
# plt.figure(figsize=(20, 20)) # size is in "inches"
# plt.imshow(img_data, cmap='gray', interpolation='nearest')
