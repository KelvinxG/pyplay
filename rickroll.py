from datetime import *

from MyQR import myqr as mq
import qrcode
import qrcode.image.svg

get_today=date.today().strftime("%A %d/%B /%y")


img=qrcode.make("https://www.youtube.com/watch?v=dQw4w9WgXcQ",image_factory=qrcode.image.svg.SvgImage)

with open("qr.svg",'wb') as qr:
	img.save(qr)
		


