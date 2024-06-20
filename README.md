<h1 align="center">Image Strip Division and Assembly</h1>
<h3 align="center">Laboratory Output #1 for Computer Vision</h3>

<p align="center">
  <img width="700" src="https://github.com/YangXLR8/Image-Processing/blob/main/Process/out/final.jpg" alt="cli output"/>
</p>

## Description

This Laboratory Output demonstrates how to divide an image into horizontal and vertical strips, and then assemble these strips back into new images. It uses the OpenCV library for image manipulation and NumPy for array operations.

## Features

- **Grayscale Conversion**: Converts the input image to grayscale.
- **Horizontal Strip Division**: Divides the image into specified number of horizontal strips.
- **Vertical Strip Division**: Divides the horizontally assembled image into specified number of vertical strips.
- **Strip Assembly**: Assembles strips into larger images horizontally or vertically.
- **Image Saving**: Saves intermediate and final assembled images to the `out` directory.
- **Display**: Displays the final assembled image using OpenCV window.

## Project Structure

- `Process/`: Main folder
- `Process/out/`: Output folder.
- `Process/TestImagejpg`: test image
- `Process/process.py`: Main script to run the Image Strip Division and Assembly
- `00-README.txt`: Laboratory Instructions
- `Sardañas_Lab1.zip`: submitted final laboratory output

## Requirements

- Python 3
- OpenCV (`cv2`)
- NumPy (`numpy`)

Install these dependencies using pip if you haven't already:

```bash
pip install opencv-python numpy
```

## Usage

1. Run the script:
```bash
python main.py
```

2. Follow the on-screen prompt to enter the number of strips.
   - (Recommended: 100, 1000, 10000, ...)

## Results

This laboratory generates the following images in the out directory:

- `horiz_left_image.jpg`: Left half of the horizontally divided image.
- `horiz_right_image.jpg`: Right half of the horizontally divided image.
- `first_merged_image.jpg`: Horizontally assembled image from horiz_left_image.jpg and horiz_right_image.png.
- `vertical_left_image.jpg`: Left half of the vertically divided image.
- `vertical_right_image.jpg`: Right half of the vertically divided image.
- `final.jpg`: Final vertically assembled image.


