QR Code Generator
A simple Python script that generates QR codes from URLs and saves them as image files.
Description
This tool allows you to quickly create QR codes for any URL. Simply provide the URL, specify a filename, and the script will generate and save a QR code image that can be scanned by any QR code reader.
Features

Generate QR codes from any URL
Customize output filename
Automatic image display after generation
Clean, black and white QR code design
Error correction built-in

Requirements

Python 3.x
qrcode library
Pillow (PIL) library

Installation

Clone or download this repository
Install required dependencies:

bashpip install qrcode[pil]
This command installs both the qrcode library and Pillow (PIL) which is required for image generation.
Usage

Run the script:

bashpython qr_code_generator.py

Enter the URL when prompted:

Enter the URL to generate QR Code: https://www.example.com

Enter the filename to save the QR code:

Enter filename to save (e.g., qrcode.png): my_qrcode.png

The QR code will be generated, saved, and automatically displayed on your screen.

Example
Enter the URL to generate QR Code: https://github.com
Enter filename to save (e.g., qrcode.png): github_qr.png
QR code saved as github_qr.png
Configuration
The script uses the following QR code settings:

version: 1 (automatically adjusts based on data)
error_correction: ERROR_CORRECT_L (~7% error correction)
box_size: 10 (size of each box in pixels)
border: 4 (thickness of the border in boxes)
fill_color: black
back_color: white

You can modify these parameters in the code to customize the appearance of your QR codes.
Error Correction Levels
The script uses ERROR_CORRECT_L which allows for approximately 7% of the QR code to be damaged while still being readable. Other options include:

ERROR_CORRECT_M: ~15% error correction
ERROR_CORRECT_Q: ~25% error correction
ERROR_CORRECT_H: ~30% error correction

Troubleshooting
Issue: Module not found error

Solution: Make sure you've installed the required libraries using pip install qrcode[pil]

Issue: Invalid URL

Solution: Ensure your URL is properly formatted (e.g., includes https:// or http://)

License
This project is open source and available for personal and commercial use.
Contributing
Feel free to fork this project and submit pull requests for any improvements!
Author
Created with Python and the qrcode library.
