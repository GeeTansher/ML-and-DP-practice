# import dependencies

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.clock import Clock  # for real time feed
from kivy.graphics.texture import Texture
from kivy.logger import Logger

import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw


# Building layout
class CamApp(App):

    def build(self):
        # Main layout components
        imgLabel = Label(text="Enter Image location:")
        self.imgLocName = TextInput(text="")

        _1stLabel = Label(text="Enter 1st text:")
        self._1stText = TextInput(
            text="Palri, Uttar Pradesh, India", multiline=False)

        _2ndLabel = Label(text="Enter 2nd text:")
        self._2ndText = TextInput(text='''9G5M+53W, Shamli Rd, Palri, Uttar Pradesh
251318, India
Lat 29.358261°
Long 77.532764°
30/10/22 03:05 PM GMT+05:30''', multiline=True)

        self.button = Button(
            text="Generate Image", on_press=self.doEverything, size_hint=(1, .1))

        self.label = Label(text="", size_hint=(1, .1))

        # Grid layout
        gridLayout = GridLayout(cols=2, size_hint=(1, .8))

        # Add items to layout
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(gridLayout)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label)

        gridLayout.add_widget(imgLabel)
        gridLayout.add_widget(self.imgLocName)
        gridLayout.add_widget(_1stLabel)
        gridLayout.add_widget(self._1stText)
        gridLayout.add_widget(_2ndLabel)
        gridLayout.add_widget(self._2ndText)

        self.width = 556
        self.height = 930

        return self.layout

    def putimg(self, image_new, path, w, h, x, y):
        img3 = cv2.imread(path)
        img3 = cv2.resize(img3, (w, h), interpolation=cv2.INTER_CUBIC)
        Img = Image.fromarray(img3)
        img = Image.fromarray(image_new)
        img.paste(Img, (x, y))
        return np.array(img)

    def puttext(self, img, x, y, word, font, size, w=0):
        image = Image.fromarray(img)
        draw = ImageDraw.Draw(image)

        # use a truetype font
        font = ImageFont.truetype(font, size)
        draw.text((x, y), word, font=font, stroke_fill='white', stroke_width=w)
        return np.array(image)

    def doEverything(self, im):
        if self.imgLocName.text == "":
            self.label.text = 'Please fill Img Loc Block...'
        else:
            # print("hello",text1)
            image = cv2.imread(self.imgLocName.text)
            image = cv2.resize(image, (self.width, self.height),
                               interpolation=cv2.INTER_CUBIC)
            overlay = image.copy()

            # Rectangle parameters
            x, y, w, h = 160, self.height-150, 385, 140
            x1, y1, w1, h1 = 450, self.height-164, 95, 13
            # A filled rectangle
            cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 0, 0), -1)
            cv2.rectangle(overlay, (x1, y1), (x1+w1, y1+h1), (0, 0, 0), -1)

            overlay = self.puttext(
                overlay, 465, 679, "GPS Map Camera", "arial.ttf", 9)
            overlay = self.puttext(
                overlay, 170, 692, self._1stText.text, "SegUIVar.ttf", 22, 1)
            overlay = self.puttext(
                overlay, 170, 725, self._2ndText.text, "SegUIVar.ttf", 15)

            alpha = 0.7  # Transparency factor.

            # Following line overlays transparent rectangle
            # over the image
            image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
            image_new = self.putimg(image_new, 'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\Transparent Work\small gps.jpg',
                                    10, 10, 452, 679)
            image_new = self.putimg(image_new, r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\Transparent Work\big map.png',
                                    141, 141, 10, 693)

            cv2.imwrite(
                r'D:\ML-and-DP-practice\Machine and Deep Learning\Practice\Transparent Work\Generated.png', image_new)
            self.label.text = 'Success'


if __name__ == '__main__':
    text = 'Palri, Uttar Pradesh, India'
    text1 = '''9G5M+53W, Shamli Rd, Palri, Uttar Pradesh
251318, India
Lat 29.358261°
Long 77.532764°
30/10/22 03:05 PM GMT+05:30'''
    CamApp().run()
