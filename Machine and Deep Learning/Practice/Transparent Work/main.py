import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
import argparse

def puttext(img, x, y, word, font, size, w=0):
    image = Image.fromarray(img)
    draw = ImageDraw.Draw(image)  

    # use a truetype font  
    font = ImageFont.truetype(font, size)  
    draw.text((x,y), word, font=font, stroke_width=w)
    return np.array(image)

 
def putimg(image_new, path, w, h, x, y):
    img3 = cv2.imread(path)
    img3 = cv2.resize(img3, (w,h), interpolation = cv2.INTER_CUBIC)
    Img = Image.fromarray(img3)
    img = Image.fromarray(image_new)
    img.paste(Img, (x,y))
    return np.array(img)


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-f", "--file", type=argparse.FileType("r"), required=True)
parser.add_argument("-t")
parser.add_argument("-y")
args = parser.parse_args()


# image = cv2.imread(r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\images\scene2.webp')
image = cv2.imread(args.file.name)

 
width=596
height=842
image = cv2.resize(image,(width,height), interpolation = cv2.INTER_CUBIC)

if(args.t != None):
    text = args.t
else:
    text = 'Palri, Uttar Pradesh, India'

if(args.y != None):
    text1 = args.y
else:
    text1 ='''9G5M+53W, Shamli Rd, Palri, Uttar Pradesh\\n251318, India\\nLat 29.358261°\\nLong 77.532764°\\n30/10/22 03:05 PM GMT+05:30'''

# print(text1)
t = text1.split("\\n")
print(t)

overlay = image.copy()

# Rectangle parameters
x, y, w, h = 160, height-150, 425, 140
x1, y1, w1, h1 = 490, height-164, 95, 13
# A filled rectangle
cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 0, 0), -1)
cv2.rectangle(overlay, (x1, y1), (x1+w1, y1+h1), (0, 0, 0), -1)

overlay = puttext(overlay,505,679,"GPS Map Camera","arial.ttf", 9)
overlay = puttext(overlay,170,695,text,"SegUIVar.ttf", 22, 1)
overlay = puttext(overlay,170,728,text1,"SegUIVar.ttf", 15, 1)


alpha = 0.7 # Transparency factor.

# Following line overlays transparent rectangle
# over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
image_new = putimg(image_new, 'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\Transparent Work\small gps.jpg',
                     10, 10, 492, 679)
image_new = putimg(image_new, r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\Transparent Work\big map.png',
                     141, 141, 10, 693)

cv2.imwrite(r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\Transparent Work\hi.png', image_new)
