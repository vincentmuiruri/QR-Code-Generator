# import the qrcode library
import qrcode
from PIL import Image

# get the URL input from the user
url = input("Enter the URL to generate QR Code: ").strip()

# creating the QR code
qr = qrcode.QRCode(
    version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
                border=4,
                )

                # adding data to the QR code
                qr.add_data(url)
                qr.make(fit=True)

                # creating an image from the QR Code instance
                img = qr.make_image(fill_color="black", back_color="white")

                # saving the image to a file
                filename = input("Enter filename to save (e.g., qrcode.png): ")
                img.save(filename)
                print(f"QR code saved as {filename}")

                # optionally display the image
                img.show()