import pyqrcode
from PIL import Image

def qrcg()
  

link = input("Enter URL: ")
qr_code = pyqrcode.create(link)

qr_code.png("QRCode.png", scale=5)

Image.open("QRCode.png")
