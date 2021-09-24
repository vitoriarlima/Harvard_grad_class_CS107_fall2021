# PROBLEM 4_animation

import numpy as np
import matplotlib.pyplot as plt
import datetime
from IPython.display import clear_output

### Closure defined up here
x=0
radian = np.pi/180



#running for 10 seconds
while x <10:
    currentDT = datetime.datetime.now()
    hour = currentDT.hour
    minute = currentDT.minute
    second = currentDT.second
    fig = plt.figure(figsize = (6,6))


    # Calculate theta in degrees for each hand

    theta_hour = 90 - 30*hour - minute/2
    theta_minute = 90 - 6*minute
    theta_second = 90 - 6*second

    #change to gradients
    #radian = np.pi/180

    #x = r * np.cos(theta)
    r = 10 

    #x = r * np.cos(theta_hour*rad) 
    #y = r * np.sin(theta_hour*rad)


    #nested function
    def get_coordinates_time(r):
        def time(theta):
            x = r * np.cos(theta*radian) 
            y = r * np.sin(theta*radian)
            return x, y
        return time   


    # Specify the length of hour, minute and second hands
    #hour_hand = get_coordinates_time(r)

    hour_hand = get_coordinates_time(10)
    x_hour, y_hour = hour_hand(theta_hour)


    minute_hand = get_coordinates_time(10)
    x_minute, y_minute = minute_hand(theta_minute)

    second_hand = get_coordinates_time(10)
    x_second, y_second = second_hand(theta_second)

    xmin = -20
    xmax = 20
    ymin = -20
    ymax = 20
    # Plot the clock
    
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([0,x_hour],[0, y_hour])
    plt.plot([0,x_minute],[0, y_minute])
    plt.plot([0,x_second],[0, y_second])
    
    x+=1
    fig.canvas.draw()
    plt.pause(1)
    clear_output(wait=True)
    