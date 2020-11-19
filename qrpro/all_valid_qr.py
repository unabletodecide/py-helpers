import sys
import os
import generate as gq
from urllib.request import urlopen
import json

base_url = "http://xyz.cloudfront.net/"
store_id = "ABCStore"
backend_url = "http://ec2-xyz.compute-n.amazonaws.com:0000/"

def get_tables(url):
	try:
		gettables_api = url+"strqrc/"+store_id+"/123"
		with urlopen(gettables_api) as myurl:
			response=myurl.read()
		data = json.loads(response)
		layout = data["org"]["layout"]
		tables = layout[0]["expanded"]
		return list(tables)
	except Exception as e:
		print(e)
		sys.exit("Backend Server URL Error")

def table_urls(base_url, alltables):
	allurls=[]
	for i in alltables:
		allurls.append(base_url+str(i))
	return allurls

def createqr(urls):
	for url in urls:
		gq.text2qr(url)
	print("Success: Check output folder")

if __name__ == '__main__':

	print(len(sys.argv))
	if (len(sys.argv) == 1):
		tables = get_tables(backend_url)
		store_url = base_url+"menu/"+store_id+"/"
		all_urls = table_urls(store_url, tables)

	elif (len(sys.argv) != 3):
		sys.exit('Need exactly 2 arguments.\n\
			1. Base URL\n\
			2. Store ID\n')
	else:
		base_url = sys.argv[1]
		store_id = sys.argv[2]
		if ('http://' not in base_url):
			sys.exit('Enter a valid base url with http://\n')
		elif (base_url[-1]!='/'):
			base_url=base_url+"/"
		else:
			store_url = base_url+"menu/"+store_id+"/"
			if (store_id == 'ABCStore'):
				backend_url = backend_url
			elif (store_id == 'DEFStore'):
				backend_url = "http:/xyz.amazonaws.com:0000/"
			elif (store_id == 'GHIStore'):
				backend_url = "http://pqr.amazonaws.com:9000/"
			else:
				sys.exit("Unknown Backend URL for this Store ID.")
			tables = get_tables(backend_url)
			all_urls = table_urls(store_url, tables)
	createqr(all_urls)
	# for text in all_urls:
	# 	gq.text2
