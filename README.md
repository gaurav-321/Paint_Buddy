# 🎨 Paint_Buddy: Automate Your Painting with Python!

## Description
Paint_Buddy is a Python program that automates the painting process in Microsoft Paint using the PyAutoGUI and OpenCV libraries. It converts black and white vector images into horizontal lines, significantly speeding up your drawing workflow.

## Features
- **Image Processing**: Converts black and white vector images into horizontal lines.
- **Automated Drawing**: Simulates mouse movements to draw on the screen based on pixel art.
- **User-Friendly Interface**: Easy-to-use script with clear instructions for installation and usage.

## 🛠️ Installation
To get started, you'll need to install Python and set up your environment. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gag3301v/Paint_Buddy.git
   cd Paint_Buddy
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Usage
Here's how you can use Paint_Buddy to automate your painting:

### Drawing with Pixel Art
1. Prepare a black and white vector image of the pixel art you want to draw.
2. Run the main script:
   ```bash
   python main.py path/to/your/image.png
   ```

### Example Code Snippet
Below is an example of how the `main.py` script works:

```python
import cv2
import numpy as np
import pyautogui
import time

def draw(number_of_pixels):
    """Moves the mouse left by the specified number of pixels."""
    pyautogui.dragRel(-number_of_pixels, 0, duration=0.1)

def next_line():
    """Moves the mouse down one pixel to prepare for the next row of pixels."""
    pyautogui.moveRel(0, 1, duration=0.1)

# Load and process the image
image = cv2.imread('path/to/your/image.png', cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Automate drawing
for row in binary_image:
    for pixel in row:
        if pixel == 0:  # Black pixel
            draw(1)
        else:  # White pixel
            next_line()
```

## 🔧 Configuration
No additional configuration is required. The script uses default settings provided by PyAutoGUI and OpenCV.

## 🧪 Tests
Tests are not available for this project as the primary focus is on automation rather than development of a library with extensive test coverage.

## 📁 Project Structure
```
Paint_Buddy/
├── main.py
├── paint_buddy.py
└── requirements.txt
```

## 👩‍💻 Contributing
Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using Paint_Buddy! Feel free to reach out if you have any questions or need further assistance.