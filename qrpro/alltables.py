import sys
import os
import generate as gq

def table_urls(base_url, min_t, max_t):
	mylist = list(range(max_t,min_t, -1))
	allurls=[]
	for i in mylist:
		allurls.append(base_url+str(i))
	return allurls

def createqr(urls):
	for url in urls:
		gq.text2qr(url)
	print("Success: Check output folder")

if __name__ == '__main__':
	print(len(sys.argv))
	if (len(sys.argv) == 1):
		base_url = "http://xyz.cloudfront.net/"
		store_id = "ABCStore"
		min_t = 15
		max_t = 99
		store_url = base_url+"menu/"+store_id+"/"
		all_urls = table_urls(store_url, min_t, max_t)

	elif (len(sys.argv) != 5):
		sys.exit('Need exactly 4 arguments.\n\
			1. Base URL\n\
			2. Store ID\n\
			3. Min Table No.\n\
			4. Max Table No.\n')
	else:
		base_url = sys.argv[1]
		store_id = sys.argv[2]
		try:
			min_t = int(sys.argv[3])
			max_t = int(sys.argv[4])
		except:
			sys.exit('pass valid data types for all fields')
		if ('http://' not in base_url):
			sys.exit('Enter a valid base url with http://\n')
		elif (min_t>max_t):
			sys.exit("miimum table value cannot be greater than maximum")
		else:
			store_url = base_url+"menu/"+store_id+"/"
			all_urls = table_urls(store_url, min_t, max_t)
	createqr(all_urls)
	# for text in all_urls:
	# 	gq.text2
