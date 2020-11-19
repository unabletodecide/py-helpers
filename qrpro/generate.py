import qrcode
import os

def text2qr(myurl):
	img = qrcode.make(myurl)
	imname = myurl.rsplit('/', 1)[-1]+'_valid'
	if ('output' not in os.listdir()):
		os.mkdir('output')
	img.save('./output/'+imname+'.png')
	print("Created QR for table "+imname)