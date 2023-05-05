import pyrcode
import png

link = "https://google.com"
qr_code = pyqrcode.create(link)
qr_code.png("image.png", scale=5)
