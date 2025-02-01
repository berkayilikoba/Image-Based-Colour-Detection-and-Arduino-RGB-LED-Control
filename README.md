# Colour Detection and Arduino RGB LED Control

This project detects the dominant colour in the center of an image using OpenCV and sends the detected colour name to an Arduino via serial communication. The Arduino then controls an RGB LED based on the detected colour.

## Features
- Reads an image and processes it using OpenCV.
- Converts the image to the HSV colour space.
- Detects the colour at the center of the image and finds the closest predefined colour (Red, Green, or Blue).
- Sends the detected colour to an Arduino via serial communication.
- Arduino controls an RGB LED based on the received colour.

## Requirements
### **Software**
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- PySerial

### **Hardware**
- Arduino board
- RGB LED
- Resistors (330Ω recommended)
- Jumper wires

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Colour-Detection-Arduino-RGB-LED-Control.git
   cd Colour-Detection-Arduino-RGB-LED-Control
   ```

2. Install the required Python libraries:
   ```bash
   pip install opencv-python numpy pyserial
   ```

3. Upload the Arduino code to your board (See `arduino_code.ino`).

## Usage
1. Place an image (`.png` or `.jpg`) in the project directory.
2. Modify the Python script to use the correct image filename.
3. Run the Python script:
   ```bash
   python color_detection.py
   ```
4. The detected colour will be sent to the Arduino, which will control the RGB LED accordingly.

## Wiring Diagram
- **Red Pin** → Arduino Digital Pin (e.g., 9)
- **Green Pin** → Arduino Digital Pin (e.g., 10)
- **Blue Pin** → Arduino Digital Pin (e.g., 11)
- **Common Cathode/Anode** → Ground / 5V (depending on LED type)

## Example Output
If the center pixel of the image is close to **red**, the Arduino will receive `red` and light up the **red** LED.

## Future Improvements
- Support for more colours.
- Improve colour detection accuracy.
- Add real-time webcam support.

## License
This project is licensed under the MIT License.
