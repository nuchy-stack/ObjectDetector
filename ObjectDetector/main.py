import cv2
from PIL import Image
from utFunction import get_limit

yellow= (255, 0, 0)  # BGR format Change to color what yuo want to detect
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limit(color=yellow)

    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    mask_= Image.fromarray(mask)

    bbox =mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 6) # the last number is the thickness of the rectangle
    print(bbox)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()

