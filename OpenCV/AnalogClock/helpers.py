import cv2
import datetime
import math
from constants import CENTER, COLORS
from constants import RADIUS


def getTicks():
    hourTicksInit = []
    hourTicksDest = []

    for i in range(0, 360, 6):
        x = int(CENTER[0] + RADIUS * math.cos(i * math.pi / 180))
        y = int(CENTER[1] + RADIUS * math.sin(i * math.pi / 180))
        hourTicksInit.append((x, y))

    for i in range(0, 360, 6):
        x = int(CENTER[0] + (RADIUS-20) * math.cos(i * math.pi / 180))
        y = int(CENTER[1] + (RADIUS-20) * math.sin(i * math.pi / 180))
        hourTicksDest.append((x, y))

    return hourTicksInit, hourTicksDest


def getDigitalTime(h, m, s):
    time = ""
    hour = ""
    minute = ""
    second = ""
    if(h < 10):
        hour = "0{}:".format(h)
    else:
        hour = "{}:".format(h)
    if(m < 10):
        minute = "0{}:".format(m)
    else:
        minute = "{}:".format(m)
    if(s < 10):
        second = "0{}".format(s)
    else:
        second = "{}".format(s)
    time = hour+minute+second
    return time


def drawFace(img):
    time = datetime.datetime.now().time()
    hour = math.fmod(time.hour, 12)
    minu = time.minute
    sec = time.second

    secAngle = math.fmod(sec * 6 + 270, 360)
    minAngle = math.fmod(minu * 6 + 270, 360)
    hourAngle = math.fmod((hour*30) + (minu/2) + 270, 360)

    sec_x = int(CENTER[0] + (RADIUS-25) * math.cos(secAngle * math.pi / 180))
    sec_y = int(CENTER[1] + (RADIUS-25) * math.sin(secAngle * math.pi / 180))
    cv2.line(img, CENTER, (sec_x, sec_y), COLORS['black'], 2, cv2.LINE_AA)

    min_x = int(CENTER[0] + (RADIUS-60) * math.cos(minAngle * math.pi / 180))
    min_y = int(CENTER[1] + (RADIUS-60) * math.sin(minAngle * math.pi / 180))
    cv2.line(img, CENTER, (min_x, min_y), COLORS['cyan'], 3, cv2.LINE_AA)

    hour_x = int(CENTER[0] + (RADIUS-100) *
                 math.cos(hourAngle * math.pi / 180))
    hour_y = int(CENTER[1] + (RADIUS-100) *
                 math.sin(hourAngle * math.pi / 180))
    cv2.line(img, CENTER, (hour_x, hour_y), COLORS['amber'], 7, cv2.LINE_AA)

    cv2.circle(img, CENTER, 5, COLORS['dark_gray'], -1)

    digitalTime = getDigitalTime(int(hour), minu, sec)

    cv2.putText(img, digitalTime, (200, 390), cv2.FONT_HERSHEY_DUPLEX,
                1.6, COLORS['red'], 1, cv2.LINE_AA)

    return img
