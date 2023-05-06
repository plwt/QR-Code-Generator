import pyqrcode
from PIL import Image

def qrcg():
    address = input("Enter URL: ")
    qr_code = pyqrcode.create(address)
    qr_code.png("image.png", scale=5)
    img = Image.open("/QR-Code-Generator/image.png")
    img.show()
    exit()

qrcg()