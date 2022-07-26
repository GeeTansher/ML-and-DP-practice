import cv2
import datetime
import math
from constants import CENTER
from constants import RADIUS

def getTicks():
    hourTicksInit = []
    hourTicksDest = []
    
    for i in range(0,360,6):
        x = int(CENTER[0] + RADIUS * math.cos(i * math.pi / 180))
        y = int(CENTER[1] + RADIUS * math.sin(i * math.pi / 180))
        hourTicksInit.append((x,y))
        
    for i in range(0,360,6):
        x = int(CENTER[0] + (RADIUS-20) * math.cos(i * math.pi / 180))
        y = int(CENTER[1] + (RADIUS-20) * math.sin(i * math.pi / 180))
        hourTicksDest.append((x,y))