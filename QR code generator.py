import pyqrcode
import png
source = "https://www.etsy.com/in-en/listing/1488717017/digital-art-print-monkey-with-tongue"
url = pyqrcode.create(source)
url.png("E:/picture.png",scale=8)
