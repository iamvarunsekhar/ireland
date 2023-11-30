
import cv2
import random
import utils as ut


# Define the dimensions of the parking lot, road and the car
PARKING_LOT_WIDTH = 300
PARKING_LOT_HEIGHT = 700
ROAD_POSITION = 100
ROAD_THICKNESS = 50
CAR_WIDTH = 10

# Define the colors of the different objects in the parking lot
ROAD_COLOUR = (255, 0, 0)
PARKING_SPACE_COLOUR = (0,255,0)
CAR_COLOUR = (120, 2, 200)
CAR_COLOUR_PARKED = (100,2,100)


def simulate_parking(n=20,side='all'):
    
    '''
        Function to simulate the parking lot and parking scenarios. 
        :param int n: Number of already parked cars
        :param str side: Which sides have parked cars. Default is both sides
    '''
    
    # Create parking lot 
    parking_lot = ut.create_parking_lot(PARKING_LOT_WIDTH, PARKING_LOT_HEIGHT,ROAD_POSITION,ROAD_THICKNESS,CAR_WIDTH,ROAD_COLOUR,PARKING_SPACE_COLOUR)
    parking_lot = ut.place_cars(n,parking_lot, CAR_WIDTH, PARKING_LOT_HEIGHT, ROAD_POSITION, ROAD_THICKNESS, CAR_COLOUR, side)
    cv2.imshow("Parking Lot", parking_lot)
    cv2.waitKey(700)
    
    # Simulate a new car entering the parking lot
    car_count=1
    while True:
        print('Car no: ' + str(car_count) + " entering")
        # Create car of random height
        CAR_HEIGHT = random.sample([10,20,30,40,50,60,70,80,90,100],1)[0]
        parking_lot = ut.park_a_car(parking_lot,ROAD_POSITION,ROAD_THICKNESS,
                                    CAR_HEIGHT,CAR_WIDTH,PARKING_LOT_WIDTH,
                                    CAR_COLOUR,PARKING_SPACE_COLOUR,CAR_COLOUR_PARKED)
        if type(parking_lot)!=int:
            cv2.imshow("Parking Lot", parking_lot)
            cv2.waitKey(700)
            car_count = car_count+1
        else:
            print("Parking lot full")
            break

if __name__=='__main__':
    simulate_parking()

