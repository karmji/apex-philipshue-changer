
import numpy as np
import requests
import json
import cv2
import os
import pyautogui

#image = cv2.imread('assets/blueEvo3.png', 1)
#This will load in the image as an unchanged image

#This image will only work in 1650 resolution with username karma

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# #Wait an infinite amount of time because of '0'
# cv2.destroyAllWindows()

with open("username.txt", 'r') as file:
    username = file.readline().strip()


URL = f"http://192.168.254.122/api/{username}/lights/3/state"

greyEvoAcquired = {"on": True,
"bri":255,
"hue":10000,
"sat":1,
"effect": "none"
}

blueEvoAcquired = {"on": True,
"bri":255,
"hue":46592,
"sat":226,
"effect": "none"
}

purpleEvoAcquired = {"on": True,
"bri":255,
"hue":50000,
"sat":226,
"effect": "none"
}

redEvoAcquired = {"on": True,
"bri":255,
"hue":1000,
"sat":226,
"effect": "none"
}

goldEvoAcquired = {"on": True,
"bri":255,
"hue":10500,
"sat":255,
"effect": "none"
}

cracked = {"on": True,
"bri":255,
"hue":10000,
"sat":1,
"effect": "none"
}

while(True):

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    
    px = pyautogui.pixel(229, 982)

    currentPixel = " ".join(map(str,px))
    
    greyEvo = "201 201 201"
    blueEvo = "32 150 255"
    purpleEvo = "167 46 255"
    redEvo = "255 3 3"
    goldEvo = "255 214 62"
    crackedEvo = "80 80 80"
    
    if currentPixel == greyEvo:
        r = requests.put(URL, json.dumps(greyEvoAcquired))
       
    if currentPixel == blueEvo:
        r = requests.put(URL, json.dumps(blueEvoAcquired))
      
    if currentPixel == purpleEvo:
        r = requests.put(URL, json.dumps(purpleEvoAcquired))
       
    if currentPixel == redEvo:
        r = requests.put(URL, json.dumps(redEvoAcquired))
       
    if currentPixel == goldEvo:
        r = requests.put(URL, json.dumps(goldEvoAcquired))
        
    if currentPixel == crackedEvo:
        r = requests.put(URL, json.dumps(cracked))
