import numpy as np
import cv2

def get_limit(color):
    # Convert the color to HSV
    hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]

    # Define a range around the color in HSV space
    lower_limit = np.array([hsv_color[0] - 10, 100, 100], dtype=np.uint8)
    upper_limit = np.array([hsv_color[0] + 10, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit