#Object Detector

This project uses **Python and OpenCV** to detect colors from live video using a webcam.

The program:
- Gets live video from a webcam.
- Reads each frame from the camera.
- Converts the image from BGR to HSV color space.
- Creates a mask to detect a specific color.
- Uses contours to find the detected color/object.
- Displays the result in real time.

## Technologies Used

- Python
- OpenCV
- NumPy
- Pillow (PIL)
- Webcam

## Installation

Install the required libraries:

```bash
pip install opencv-python numpy Pillow
