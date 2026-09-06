import cv2
import numpy as np
img = cv2.imread("pic/img6.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshed = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 3000:  # Filter out small contours
        #cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)  # Draw the contour on the original image
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)  # Draw a bounding rectangle around the contour
cv2.imshow("Original", img)
cv2.imshow("Thresholded", threshed)
cv2.waitKey(0)

