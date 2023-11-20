
import cv2
import random
import numpy as np
import time

# Define the dimensions of the parking lot
PARKING_LOT_WIDTH = 550
PARKING_LOT_HEIGHT = 700
ROAD_WIDTH = 330
ROAD_LENGTH = int(PARKING_LOT_HEIGHT/2)
road_thickness = 50
car_height = 20
car_width = 10
toll_height = 300
toll_width = 100

# Define the colors of the different objects in the parking lot
EMPTY_SPOT_COLOR = (0, 0, 0)
OCCUPIED_SPOT_COLOR = (0, 0, 255)
ROAD_COLOR = (255, 0, 0)
TOLL_COLOR = (0,255,0)
PARKING_SPACE_COLOR = (0,255,0)
CAR_COLOR = (120, 2, 200)
CAR_COLOR_PARKED = (100,2,100)


def move_event(event, x, y, flags, params):
    imgk = image.copy()
    # checking for right mouse clicks     
    if event==cv2.EVENT_MOUSEMOVE:
  
        # displaying the coordinates
        # on the Shell
        # print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (x, y)
        B = imgk[y, x, 0]
        G = imgk[y, x, 1]
        R = imgk[y, x, 2]

    cv2.putText(imgk, '(x, y)=({}, {})'.format(x, y), org, font, 1, (255, 255, 255), 1, cv2.LINE_8)
    cv2.putText(imgk, '                  ,R={}'.format(R), org, font, 1, (0, 0, 255), 1, cv2.LINE_8)
    cv2.putText(imgk, '                         ,G={}'.format(G), org, font, 1, (0, 255, 0), 1, cv2.LINE_8)
    cv2.putText(imgk, '                                 ,B={}'.format(B), org, font, 1, (255, 0, 0), 1, cv2.LINE_8)
    cv2.imshow('image', imgk)
    
    
# Create a blank image to represent the parking lot
parking_lot = np.zeros((PARKING_LOT_WIDTH, PARKING_LOT_HEIGHT, 3), dtype=np.uint8)

# Draw the road in the middle of the parking lot
cv2.rectangle(parking_lot, (ROAD_WIDTH, 0), (ROAD_WIDTH+road_thickness, ROAD_LENGTH), ROAD_COLOR, -1)

cv2.rectangle(parking_lot, (20,PARKING_LOT_HEIGHT-2),(20,PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)
cv2.rectangle(parking_lot, ((20+toll_width),PARKING_LOT_HEIGHT-2),((20+toll_width),PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)

cv2.rectangle(parking_lot, (200+toll_width,PARKING_LOT_HEIGHT-2),(200+toll_width,PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)
cv2.rectangle(parking_lot, ((200+toll_width*2),PARKING_LOT_HEIGHT-2),((200+toll_width*2),PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)

cv2.rectangle(parking_lot, (440+100,PARKING_LOT_HEIGHT-2),(440+100,PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)
cv2.rectangle(parking_lot, (440+200,PARKING_LOT_HEIGHT-2),(440+200,PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)

cv2.rectangle(parking_lot, (440+200,PARKING_LOT_HEIGHT-2),(440+200,PARKING_LOT_HEIGHT-2-toll_height),TOLL_COLOR,-1)

initial = cv2.rectangle(parking_lot.copy(), (300,400),(400,400),TOLL_COLOR,-1)
cv2.rectangle(initial, (540,400),(640,400),TOLL_COLOR,-1)

toll = [20,300,540]
toll_status = {1:'Open',2:'Closed',3:'Closed'}
toll_count = {1:0,2:0,3:0}


while True:
    
    car = cv2.rectangle(initial, (ROAD_WIDTH+15,0), (ROAD_WIDTH+15+car_width,0+car_height), CAR_COLOR, -1)
    car_x = ROAD_WIDTH + 15
    car_y = 0
    while(car_y<=380)
        car_y += 10
        car = cv2.rectangle(parking_lot.copy(), (ROAD_WIDTH+15,car_y), (ROAD_WIDTH+15+car_width,car_y+car_height), CAR_COLOR, -1)
        image=initial
        cv2.imshow('image', image)
        cv2.setMouseCallback('image', move_event)
        cv2.waitKey(1000)
    open_tolls = [k for k,v in toll_status.items() if v=='Open']
    if len(open_tolls)>1:
        optimal = [k for k in open_tolls if toll_count[k]<3]
    else:
        optimal = open_tolls
    go_to = random.sample(optimal,1)[0]
    
    if go_to==1:
        
# displaying the image
image=initial
cv2.imshow('image', image)
cv2.setMouseCallback('image', move_event)
cv2.waitKey(0)

