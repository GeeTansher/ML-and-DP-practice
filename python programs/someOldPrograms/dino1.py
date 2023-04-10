from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
class Bot:
    """Bot for playing Chrome dino run game"""
    def __init__(self):
        self.restart_coords = (480, 503)
        self.dino_coords = (207, 534)  
        self.area = (self.dino_coords[0] + 90, self.dino_coords[1],
                     self.dino_coords[0] + 150, self.dino_coords[1] + 5)
Get started
Becoming Human: Artificial Intelligence Magazine
Google Chrome dinosaur game Python bot.
Taras Rumezhak
Taras Rumezhak
Jul 18 · 4 min read

Hello everybody, today we are going to build very simple python bot. We won’t use deep learning. It is a very simple bot which uses only screen processing.

I consider this tutorial to be a great start for beginners because it’s very easy, but yet very exciting.
There are about fifty lines of code, only one bot class and nothing else. So let’s start.
As always, we need some libraries to be imported.
Trending AI Articles:
1. Deep Learning Book Notes, Chapter 1
2. Deep Learning Book Notes, Chapter 2
3. Machines Demonstrate Self-Awareness
4. Visual Music & Machine Learning Workshop for Kids
Here they are:
from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
We need PIL library to grab our play area and process it. The second library is pyautogui, it’s a great tool for controlling mouse and keyboard by your code. Time library is necessary for us to make some delays between executing the code blocks. And numpy will convert our image to array for easier processing. And let’s go on to our class:
class Bot:
    """Bot for playing Chrome dino run game"""
    def __init__(self):
        self.restart_coords = (480, 503)
        self.dino_coords = (207, 534)  
        self.area = (self.dino_coords[0] + 90, self.dino_coords[1],
                     self.dino_coords[0] + 150, self.dino_coords[1] + 5)
When initializing the class object we need to specify some important parameters: the coordinates of the restart button, the coordinates of the dinosaur, and the coordinates of the rectangle area where obstacles will be detected. Frankly speaking, we don't need to use our mouse for clicking the restart button, because we can do it by pressing space instead. But it will be good for you to know how to control the mouse for your own bots for other projects.
NOTE: in the code above there are coordinates for my monitor. For your bot they can be different. You can use Screen Loupe (http://www.gregorybraun.com/Loupe.html) to discover the coordinates of particular pixel or you can use some image redactor to do it.
def set_dino_coords(self, x, y):
    """
    Change default dino coordinates
    :param x: top right x coordinate (int)
    :param y: top right y coordinate (int)
    :return: None
    """
    self.dino_coords = (x, y)

def set_restart_coords(self, x, y):
    """
    Change default restart button coordinates
    :param x: center x coordinate (int)
    :param y: center y coordinate (int)
    :return: None
    """
    self.restart_coords = (x, y)

def restart(self):
    """
    Restart the game and set default crawl run
    :return: None
    """
    pyautogui.click(self.restart_coords)
    pyautogui.keyDown('down')
Get started
Becoming Human: Artificial Intelligence Magazine
Google Chrome dinosaur game Python bot.
Taras Rumezhak
Taras Rumezhak
Jul 18 · 4 min read

Hello everybody, today we are going to build very simple python bot. We won’t use deep learning. It is a very simple bot which uses only screen processing.

I consider this tutorial to be a great start for beginners because it’s very easy, but yet very exciting.
There are about fifty lines of code, only one bot class and nothing else. So let’s start.
As always, we need some libraries to be imported.
Trending AI Articles:
1. Deep Learning Book Notes, Chapter 1
2. Deep Learning Book Notes, Chapter 2
3. Machines Demonstrate Self-Awareness
4. Visual Music & Machine Learning Workshop for Kids
Here they are:
from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
We need PIL library to grab our play area and process it. The second library is pyautogui, it’s a great tool for controlling mouse and keyboard by your code. Time library is necessary for us to make some delays between executing the code blocks. And numpy will convert our image to array for easier processing. And let’s go on to our class:
class Bot:
    """Bot for playing Chrome dino run game"""
    def __init__(self):
        self.restart_coords = (480, 503)
        self.dino_coords = (207, 534)  
        self.area = (self.dino_coords[0] + 90, self.dino_coords[1],
                     self.dino_coords[0] + 150, self.dino_coords[1] + 5)
When initializing the class object we need to specify some important parameters: the coordinates of the restart button, the coordinates of the dinosaur, and the coordinates of the rectangle area where obstacles will be detected. Frankly speaking, we don't need to use our mouse for clicking the restart button, because we can do it by pressing space instead. But it will be good for you to know how to control the mouse for your own bots for other projects.
NOTE: in the code above there are coordinates for my monitor. For your bot they can be different. You can use Screen Loupe (http://www.gregorybraun.com/Loupe.html) to discover the coordinates of particular pixel or you can use some image redactor to do it.
def set_dino_coords(self, x, y):
    """
    Change default dino coordinates
    :param x: top right x coordinate (int)
    :param y: top right y coordinate (int)
    :return: None
    """
    self.dino_coords = (x, y)

def set_restart_coords(self, x, y):
    """
    Change default restart button coordinates
    :param x: center x coordinate (int)
    :param y: center y coordinate (int)
    :return: None
    """
    self.restart_coords = (x, y)

def restart(self):
    """
    Restart the game and set default crawl run
    :return: None
    """
    pyautogui.click(self.restart_coords)
    pyautogui.keyDown('down')
I specified additional methods to let you set your own coordinates. You can play with it a little bit and explore which are the best. Read method documentation! And restart method just makes the mouse click at particular coordinates and make our dinosaur crawl.
def jump(self):
    """
    Jump over the obstacle
    :return: None
    """
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.095)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def detection_area(self):
    """
    Checks the area to have obstacles
    :return: float
    """
    image = ImageGrab.grab(self.area)
    gray_img = ImageOps.grayscale(image)
    arr = np.array(gray_img.getcolors())
    # print(arr.mean())
    return arr.mean()
def main(self):
    """
    Main loop of the playing
    :return: None
    """
    self.restart()
    while True:
        if self.detection_area() < 273:
            self.jump()
 
bot = Bot()
bot.main()