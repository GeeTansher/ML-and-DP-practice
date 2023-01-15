import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
import argparse


def puttext(img, x, y, word, font, size, w=0):
    image = Image.fromarray(img)
    draw = ImageDraw.Draw(image)

    # use a truetype font
    font = ImageFont.truetype(font, size)
    draw.text((x, y), word, font=font, stroke_width=w)
    return np.array(image)


def putimg(image_new, path, w, h, x, y):
    img3 = cv2.imread(path)
    img3 = cv2.resize(img3, (w, h), interpolation=cv2.INTER_CUBIC)
    Img = Image.fromarray(img3)
    img = Image.fromarray(image_new)
    img.paste(Img, (x, y))
    return np.array(img)


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-f", "--file", type=argparse.FileType("r"), required=True, help='Enter image path')
parser.add_argument("-t", type=str, help='Enter 1st Location if not Palri')
parser.add_argument("-y", type=str, help='Enter 2nd Location Text if not related to Palri')
args = parser.parse_args()


# image = cv2.imread(r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\images\scene2.webp')
image = cv2.imread(args.file.name)

path = args.file.name.split('\\')
path[-1] = 'Generated_' + path[-1].split('.')[0] + '.png'
ResultPath = ""
for n in path:
    if n == path[-1]:
        ResultPath = ResultPath+n
    else:
        ResultPath = ResultPath+n+'\\'


if (args.t != None):
    text = args.t
else:
    text = 'Palri, Uttar Pradesh, India'

if (args.y != None):
    text1 = args.y
    t = text1.split("\\n")
    text1 = ""
    for t1 in t:
        if t1 == t[-1]:
            text1 = text1+t1
        else:
            text1 = text1+t1+'\n'
else:
    text1 = '''9G5M+53W, Shamli Rd, Palri, Uttar Pradesh
251318, India
Lat 29.358261
Long 77.532764
30/10/22 03:05 PM GMT+05:30'''


if(image.shape[0] >= image.shape[1]):
    width = 556
    height = 930
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

    overlay = image.copy()

    # Rectangle parameters
    x, y, w, h = 160, height-150, 385, 140
    x1, y1, w1, h1 = 450, height-164, 95, 13
    # A filled rectangle
    cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 0, 0), -1)
    cv2.rectangle(overlay, (x1, y1), (x1+w1, y1+h1), (0, 0, 0), -1)

    overlay = puttext(overlay, 465, 767, "GPS Map Camera", "arial.ttf", 9)
    overlay = puttext(overlay, 170, 780, text, "segoeui.ttf", 22, 1)
    overlay = puttext(overlay, 170, 813, text1, "segoeui.ttf", 15)


    alpha = 0.7  # Transparency factor.

    # Following line overlays transparent rectangle
    # over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    image_new = putimg(image_new, 'D:\working data\SOFTWARE1\geetansh map software\Transparent Work\small gps.jpg',
                    10, 10, 452, 767)
    image_new = putimg(image_new, r'D:\working data\SOFTWARE1\geetansh map software\Transparent Work\big map.png',
                    141, 141, 10, 781)
else:
    width = 1100
    height = 556
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
    overlay = image.copy()

    # Rectangle parameters
    # x, y, w, h = 160, width-150, 185, 140
    x, y, w, h = 170, height-150, 920, 140
    x1, y1, w1, h1 = 967, height-168, 123, 17
    # A filled rectangle
    cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 0, 0), -1)
    cv2.rectangle(overlay, (x1, y1), (x1+w1, y1+h1), (0, 0, 0), -1)

    overlay = puttext(overlay, 986, 390, "GPS Map Camera", "arial.ttf", 12)
    overlay = puttext(overlay, 180, 404, text, "SegUIVar.ttf", 24, 1)
    overlay = puttext(overlay, 180, 435, text1, "SegUIVar.ttf", 16)


    alpha = 0.7  # Transparency factor.

    # Following line overlays transparent rectangle
    # over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
    image_new = putimg(image_new, 'D:\working data\SOFTWARE1\geetansh map software\Transparent Work\small gps.jpg',
                    13, 13, 970, 390)
    image_new = putimg(image_new, r'D:\working data\SOFTWARE1\geetansh map software\Transparent Work\big map.png',
                    141, 141, 10, 404)
    
cv2.imwrite(ResultPath, image_new)
print("Success")