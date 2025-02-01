import cv2 as cv
import numpy as np 
import serial 
import time

# Initialize serial communication with Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)

# Define HSV values for basic colors
colors_hsv = {
    "red": {"h": 0, "s": 255, "v": 255},
    "green": {"h": 60, "s": 255, "v": 255},
    "blue": {"h": 120, "s": 255, "v": 255}
}

def closest_colour(hue, sat, val):
    """Find the closest predefined color based on HSV values."""
    min_distance = float('inf')
    closest_colour = None
    
    for colour, hsv in colors_hsv.items():
        distance = np.sqrt((hsv["h"] - hue)**2 + (hsv["s"] - sat)**2 + (hsv["v"] - val)**2)
        
        if distance < min_distance:
            min_distance = distance
            closest_colour = colour
            
    return closest_colour

# Load the image
image = cv.imread("green.png")

# Resize the image for better processing
resized = cv.resize(image, (600, 400))

# Convert the image from BGR to HSV color space
hsv_image = cv.cvtColor(resized, cv.COLOR_BGR2HSV)

# Get image dimensions
height = hsv_image.shape[1]  # Width of the image
width = hsv_image.shape[0]   # Height of the image

# Determine the center pixel position
hh = height // 2
ww = width // 2

# Get HSV values of the center pixel
center_pixel = hsv_image[ww, hh]
h, s, v = center_pixel[0], center_pixel[1], center_pixel[2]

# Find the closest predefined color
colour = closest_colour(h, s, v)

# Draw a circle at the center pixel
cv.circle(resized, (hh, ww), 5, (255, 255, 255), 3)

# Send the detected color to Arduino
arduino.write(colour.encode())

# Display the image
cv.imshow("image", resized)
cv.waitKey(0)

# Send 'off' signal to Arduino before closing
arduino.write(b'off')

# Close the serial communication
arduino.close()
