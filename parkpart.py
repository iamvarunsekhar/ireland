
import cv2
import random
import numpy as np
import time

# Define the dimensions of the parking lot
PARKING_LOT_WIDTH = 550
PARKING_LOT_HEIGHT = 700
ROAD_WIDTH = 100
road_thickness = 50
car_height = 20
car_width = 10

# Define the colors of the different objects in the parking lot
EMPTY_SPOT_COLOR = (0, 0, 0)
OCCUPIED_SPOT_COLOR = (0, 0, 255)
ROAD_COLOR = (255, 0, 0)
PARKING_SPACE_COLOR = (0,255,0)
CAR_COLOR = (120, 2, 200)
CAR_COLOR_PARKED = (100,2,100)


# Create a blank image to represent the parking lot
parking_lot = np.zeros((PARKING_LOT_WIDTH, PARKING_LOT_HEIGHT, 3), dtype=np.uint8)

# Draw the road in the middle of the parking lot
cv2.rectangle(parking_lot, (ROAD_WIDTH, 0), (ROAD_WIDTH+road_thickness, PARKING_LOT_HEIGHT), ROAD_COLOR, -1)
cv2.rectangle(parking_lot, (ROAD_WIDTH+road_thickness+15, 0), (ROAD_WIDTH+road_thickness+15+car_width, PARKING_LOT_HEIGHT), PARKING_SPACE_COLOR, -1)
cv2.rectangle(parking_lot, (ROAD_WIDTH-15, 0), (ROAD_WIDTH-15-car_width, PARKING_LOT_HEIGHT), PARKING_SPACE_COLOR, -1)

# Randomly place 15 cars in the parking lot
for i in range(15):
    x = random.sample([ROAD_WIDTH+road_thickness+15,ROAD_WIDTH-15-car_width],1)[0]
    y = random.sample(np.arange(0,PARKING_LOT_HEIGHT-30,30).tolist(),1)[0]
    print(x,y)
    cv2.rectangle(parking_lot, (x, y), (x +car_width, y + car_height), CAR_COLOR, -1)
cv2.imshow("Parking Lot", parking_lot)
cv2.waitKey(2000)

# Define a function to simulate a new car entering the parking lot
def simulate_new_car(parking_lot):
    

    # Create a new car
    car = cv2.rectangle(parking_lot.copy(), (ROAD_WIDTH+15,0), (ROAD_WIDTH+15+car_width,0+car_height), CAR_COLOR, -1)
    cv2.imshow("Parking Lot", car)
    cv2.waitKey(2000) 

    # Start the car at the entrance of the parking lot
    car_x = ROAD_WIDTH + 15 + road_thickness
    car_y = 0

    # While the car has not found a spot, keep moving it forward
    while True:
        # Check if there is an empty spot on either side of the car
        empty_spot_left = car[car_y:car_y + car_height,ROAD_WIDTH-15-car_width:ROAD_WIDTH-15][:, 0] == PARKING_SPACE_COLOR
        empty_spot_right = car[car_y:car_y + car_height,car_x:car_x+car_width][:, 0] == PARKING_SPACE_COLOR

        # If there is an empty spot on either side, park the car there
        if all(empty_spot_left.flatten())==True:
            print('park left')
            cv2.rectangle(parking_lot, (ROAD_WIDTH-15-car_width, car_y), (ROAD_WIDTH-15, car_y + car_height), CAR_COLOR_PARKED, -1)
            cv2.imshow("Parking Lot", parking_lot)

            break
        elif all(empty_spot_right.flatten())==True:
            print('park right')
            cv2.rectangle(parking_lot, (car_x, car_y), (car_x+car_width, car_y + car_height), CAR_COLOR_PARKED, -1)

            break

        # Otherwise, move the car forward
        car_y += 10
        print('here')
        car = cv2.rectangle(parking_lot.copy(), (ROAD_WIDTH+15,car_y), (ROAD_WIDTH+15+car_width,car_y+car_height), CAR_COLOR, -1)

        # If the car reaches the end of the parking lot, it gives up and leaves
        if car_y-car_height >= PARKING_LOT_HEIGHT:
            break
        cv2.imshow("Parking Lot", car)
        cv2.waitKey(2000) 

    return parking_lot

# Simulate a new car entering the parking lot
while True:
    parking_lot = simulate_new_car(parking_lot)
    cv2.imshow("Parking Lot", parking_lot)
    cv2.waitKey(2000)

# # Display the parking lot
# cv2.imshow("Parking Lot", parking_lot)
# cv2.waitKey(0)
