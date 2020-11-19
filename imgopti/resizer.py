import os
import sys
from PIL import Image

d = './DRINKS/'
dirs = [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]

for cat_path in dirs:
	files = os.listdir(cat_path)
	#print(files)
	for filename in files:
		impath = os.path.join(cat_path, filename)
		#print (impath)
		image = Image.open(impath)
		image.thumbnail((400, 400))
		image.save(impath, optimize=True, quality=95)
		print("File saved "+impath)
		print(image.size)
		print(sys.getsizeof(image.tobytes()))