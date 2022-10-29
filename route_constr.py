import numpy
import random

def df(arg1,arg2):# Arg1 = essays, arg2 =steps
    x = 0
    y = 0
    dist_list = []
    for k in range(0,arg1):
        for c in range(0,arg2):
            haz = random.randrange(1, 5)
            if (haz == 1):
                x = x + 1
            elif (haz == 2):
                y = y + 1
            elif (haz == 3):
                x = x - 1
            elif (haz == 4):
                y = y - 1
            dist = round(pow(pow(x,2) + pow(y,2), 0.5),2)
       # dist_list.append(dist)
   # print(dist)
    return([arg2,dist])