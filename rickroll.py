


import qrcode
import qrcode.image.svg




img=qrcode.make("https://www.youtube.com/watch?v=dQw4w9WgXcQ",image_factory=qrcode.image.svg.SvgImage)

with open("qr.svg",'wb') as qr:
	img.save(qr)
		


