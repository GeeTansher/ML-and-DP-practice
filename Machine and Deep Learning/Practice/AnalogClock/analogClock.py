import cv2
import numpy as np
from constants import COLORS, CANVAS_SIZE, RADIUS, CENTER
from helpers import getTicks, drawFace

img = np.zeros(CANVAS_SIZE, dtype=np.uint8)
img[:] = [255, 255, 255]

hourTicksInit, hourTickDest = getTicks()

for i in range(len(hourTickDest)):
    if i % 5 == 0:
        cv2.line(img, hourTicksInit[i], hourTickDest[i],
                 COLORS['black'], 3, cv2.LINE_AA)
        if i==0:
            cv2.putText(img, "3", (hourTickDest[i][0]-30,hourTickDest[i][1]+5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, COLORS['magenta'], 1, cv2.LINE_AA)
        elif i==15:
            cv2.putText(img, "6", (hourTickDest[i][0]-5,hourTickDest[i][1]-30),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, COLORS['magenta'], 1, cv2.LINE_AA)
        elif i==30:
            cv2.putText(img, "9", (hourTickDest[i][0]+20,hourTickDest[i][1]+5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, COLORS['magenta'], 1, cv2.LINE_AA)
        elif i==45:
            cv2.putText(img, "12", (hourTickDest[i][0]-10,hourTickDest[i][1]+30),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, COLORS['magenta'], 1, cv2.LINE_AA)
              
    else:
        cv2.circle(img, hourTicksInit[i], 5, COLORS['black'], -1, cv2.LINE_AA)

cv2.circle(img, CENTER, (RADIUS+10), COLORS['yellow'], 2, cv2.LINE_AA)
cv2.putText(img, "TITAN", (230, 230), cv2.FONT_HERSHEY_COMPLEX,
            2, COLORS['dark_gray'], 1, cv2.LINE_AA)

while True:
    image = img.copy()
    image = drawFace(image)
    cv2.imshow("Clock", image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
