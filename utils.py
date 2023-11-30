import numpy as np
import cv2
import random
import time

# Create a new parking lot
def create_parking_lot(width, height, road_position, road_width, car_width, road_colour, parking_colour):
    '''
        Function to create a parking lot image. 
        :param str width,road_width,car_width: Widths of all objects
        :param str height: Height of the parking lot and road
        :param str road_colour, parking_colour: Colours of road and the lot
        :param str road_position: Position of the road inside the lot
    '''
    
    parking_lot = np.zeros((width,height, 3), dtype=np.uint8)
    cv2.rectangle(parking_lot, (road_position, 0), (road_position+road_width, height), road_colour, -1)
    cv2.rectangle(parking_lot, (road_position+road_width+15, 0), (road_position+road_width+15+car_width, height), parking_colour, -1)
    cv2.rectangle(parking_lot, (road_position-15, 0), (road_position-15-car_width, height), parking_colour, -1)
    return parking_lot

# Randomly place n cars in the parking lot
def place_cars(n,parking_lot, car_width, parking_lot_height, road_position, road_width, car_colour, side='all'):
    '''
        Function to randomly place n cars inside the parking lot. 
        :param obj parking_lot: parking_lot image object
        :param int n: Number of parked cars
        :param str road_width,car_width: Widths of all objects
        :param str parking_lot_height: Height of the parking lot and road
        :param str car_colour: Colours of the parked car
        :param str road_position: Position of the road inside the lot
        :param str side: Which sides car park into. Either 'left','right' or 'all'.
    '''
    
    for i in range(n):
        # Generate car of random size
        car_height = random.sample([10,20,30,40,50,60,70,80,90,100],1)[0]
        if side=='all':
            x = random.sample([road_position+road_width+15,road_position-15-car_width],1)[0]
        elif side=='left':
            x = road_position+road_width+15
        else:
            x = road_position-car_width-15
        y = random.sample(np.arange(0,parking_lot_height-30,30).tolist(),1)[0]
        cv2.rectangle(parking_lot, (x, y), (x +car_width, y + car_height), car_colour, -1)
    return parking_lot

# Function that parks a new car
def park_a_car(parking_lot,road_position, road_width, car_height, car_width, parking_lot_height, car_colour,park_colour,car_colour_parked):
    '''
        Function that checks for spaces inside the lot for an incoming car and parks it. 
        :param obj parking_lot: parking_lot image object
        :param str road_width,car_width: Widths of all objects
        :param str parking_lot_height,car_height: Height of the parking lot, road and car
        :param str car_colour,park_colour and car_color_parked: Colours of the parked cars, incoming car and incoming car after it is parked
        :param str road_position: Position of the road inside the lot
    '''
    # Create a new car at the entrance
    car = cv2.rectangle(parking_lot.copy(), (road_position+15,0), (road_position+15+car_width,car_height), car_colour, -1)
    cv2.imshow("Parking Lot", car)
    cv2.waitKey(700) 
    
    # Save initial position of the car
    car_x = road_position + road_width
    car_y = 0

    # While the car has not found a spot, keep moving it forward
    while True:
        # Check if there is an empty spot on either side of the car
        empty_spot_left = car[car_y:car_y + car_height, road_position-car_width-15:road_position-15][:, 0] == park_colour
        empty_spot_right = car[car_y:car_y + car_height, car_x+15:car_x+car_width+15][:, 0] == park_colour

        # If there is an empty spot on either side, park the car there
        if all(empty_spot_left.flatten())==True:
            print('Space available on left with coordinate: ',str(car_y))
            cv2.rectangle(parking_lot, (road_position-15-car_width, car_y), (road_position-15, car_y + car_height), car_colour_parked, -1)
            cv2.imshow("Parking Lot", parking_lot)
            break
        
        elif all(empty_spot_right.flatten())==True:
            print('Space available on right with coordinate: ',str(car_y))
            cv2.rectangle(parking_lot, (car_x+15, car_y), (car_x+15+car_width, car_y + car_height), car_colour_parked, -1)
            cv2.imshow("Parking Lot", parking_lot)
            break

        # Otherwise, move the car forward
        if car_y==0:
            print('Moving car forward')
        car_y += 10
        car = cv2.rectangle(parking_lot.copy(), (road_position+15,car_y), (road_position+15+car_width,car_y+car_height), car_colour, -1)

        # If the car reaches the end of the parking lot, it gives up and leaves
        if car_y >= parking_lot_height-(1*car_height):
            print('No space available for the car. Car exiting.')
            return -1
        cv2.imshow("Parking Lot", car)
        cv2.waitKey(100) 

    return parking_lot