# penetration testing tool for Finding Shells uploded 
# GitHub : mhndit
# Twitter : mhnd_it

import requests,re,httplib,sys,os,urllib,datetime
from bs4 import BeautifulSoup
from datetime import date
from dateutil.rrule import rrule, MONTHLY

Optins = """

 __        ______            _                 
 \ \      / /  _ \ ___ _ __ (_)_ __   ___ _ __ 
  \ \ /\ / /| |_) / __| '_ \| | '_ \ / _ \ '__|
   \ V  V / |  __/\__ \ | | | | |_) |  __/ |   
    \_/\_/  |_|   |___/_| |_|_| .__/ \___|_|   
                              |_|              
							  
[+]  WPsniper v 2.0
[+]  wordpress Tool for Finding PHP Shells Or Malicious files 
[+]  This script was written By Mohannad alOtaibi , Twitter : mhnd_it
-----------------------------------------------------------------------
"""

def UrlTest(url):
	try:
		urlOpen = urllib.urlopen(url)
		UrlCheck = urlOpen.getcode()
		if UrlCheck != 404:
			return True
		else :
			return False
	except:
		return False

def MhndIt(url):
    soup = BeautifulSoup(requests.get(url).text,"lxml")
    hrefs = []
    for a in soup.find_all('a'):
        hrefs.append(a['href'])
    return hrefs

def WPsniper(Tar):
	global a,b
	global TotalShels
	if UrlTest(Tar) == True :
		print("[+] Has Been connected ! ....")
		print("[+] will be start from : "+str(a)+" Until :"+ str(b))
		file = open('result.txt','a')
		file.write(Optins)
		for dt in rrule(MONTHLY, dtstart=a, until=b):
			line =  Tar + "/wp-content/uploads/"+dt.strftime("%Y/%m/")
			dir = "/wp-content/uploads/"+dt.strftime("%Y/%m/")
			if UrlTest(line) == True :
				DirList1 = MhndIt(line)
				for link in DirList1:
					xphp = ['.php','.php3','.phtml']
					for pattern in xphp:
						if re.search(pattern,  link):
							TotalShels+=  "[+] " + line + link+" \n"
							print("[+] " + line + link+" ")
							file = open('result.txt','a')
							file.write(line + link+" \n")
							file.close()
						#else :
							#print("[-] "+dir+" "+link+"]")
			else :
				print("[*] Scaning ... "+line+" ")
				
		print("[+] Done !")
		return True
	else :
		print("[-] website dose't Work ! " + Tar + "\n")

print Optins

if len(sys.argv) == 3 :
	wp_web = sys.argv[1]
	wp_Date = sys.argv[2]
	x = datetime.datetime.now()
	a = date(int(wp_Date), 1, 1)
	b = date(x.year, x.month, x.day)
	TotalShels = ""
	
	if WPsniper(wp_web) == True :
		print("\n[ Total files found are : ] ")
		print TotalShels
		print("[ You will find it here : result.txt ]") 
else:
	print("Usege 	: WPsniper.py [ Target ] [ From Year ] ")
	print("Example  : WPsniper.py http://example.com/wp 2017 ")
