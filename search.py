import string, random, urllib, os, thread, array, sys
if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python " + sys.argv[0] + " (Number of threads)")
threadAmount = int(sys.argv[1])


noneWorking = [0, 503, 4939, 4940, 4941, 12003, 5556, 5082]


def scrapePictures():
	while True:
		amount = int(''.join(random.choice('5' + '6') for _ in range(1)))
		if amount == 6:
			picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(3)))
			picture2 = str(''.join(random.choice(string.digits + string.lowercase) for _ in range(3)))
			name = picture + picture2
		else:
			picture = str(''.join(random.choice(string.ascii_uppercase + string.digits + string.lowercase) for _ in range(5)))
			name = picture
		printsc = "http://i.imgur.com/" + name + ".jpg"
		urllib.urlretrieve(""+ printsc, str(name) + ".jpg")
		file = os.path.getsize(str(name)+ ".jpg")
		if file in noneWorking:
			os.remove(name + ".jpg")	
		else:
			print ("[+] " + printsc)



tempVar2 = 1
print ('start ' + str(threadAmount))
while (tempVar2 <= threadAmount):
	try:
		thread.start_new_thread(scrapePictures, ())
		tempVar2 += 1
	except:
		print ("Error")


while (True):
	temp = 1+1
