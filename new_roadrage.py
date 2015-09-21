import random
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import math

class Car():
    '''
    Responsibilities:
    - set max speed - init
    - define vehicle size - init
    - keep track of velocity - set_velocity
    - keep track of position
    - deal with acceleration or slowing - set_accel
    - maintain minimum spacing with car in front

    '''
    def __init__(self, max_v = 33.3, length = 5, accel_rate = 2):
        '''
        set max speed, length of car, standard acceleration rate of 2 m/s/s

        '''
        self.max_v = max_v # m/s
        self.length = length # m
        self.accelerate = accel_rate #m/s/s

    def set_accel(self, current_v):
        '''
        10% chance to reduce speed by 2.
        if not speed up by accel_rate to max of top speed.
        '''
        if random.random() <= .1:
            current_v -= 2
            if current_v < 0:
                current_v = 0
            else:
                return current_v
        else:
            current_v += self.accelerate
            if current_v > self.max_v:
                current_v = self.max_v
                return current_v
            else:
                return current_v


    def set_velocity(self, distance, velocity):
        '''
        uses set_accel to set the new velocity for the car.
        compare distance to next car and new velocity.
        set to the distance to the rear bumper of the next car or
        or new_v, whichever is lower
        '''
        new_v = self.set_accel(velocity)
        if distance <= new_v:
            return distance
        else:
            return new_v


    # def movement(self):
    #     self.pos += self.current_v
    #     if self.pos > 1000:
    #         self.pos = (self.pos % 1000)
    #     return self.pos
    #
    #




class Simulator:
    def __init__(self, cars, road, n = 60):
        self.cars = cars
        self.road = road
        self.data = np.array([0 for x in range(1000)])

    def create_cars(number = 30):
        '''
        makes 30 cars 0 - 29

        '''
        car_list = [Car() for _ in range(number)]
        return car_list

    def start_positions():
        '''
        stars cars evenly spaced on road with numpy.linspace
        (start, stop, number)
        '''
        self.data[0][0] = int(np.linspace(5, 995, 30))


    def car_distance(self, ticks, car, car2):
        '''
        checks how far apart cars are.
        use the front bumper as the datum.

        position - size = back bumper location

        '''
        back = self.data[0][ticks -1][car2] - self.cars[car2].length
        distance = back - self.data[0][ticks-1][car]

        if distance <= 0:
            distance += self.road
        return distance
