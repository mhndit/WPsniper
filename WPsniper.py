# @mhnd_it #
import requests,re,httplib,sys,os,urllib
from bs4 import BeautifulSoup
from urlparse import urlparse

print '''
|===================================================|
[+]  WPSniper v 1.0
[+]  Tool for Finding PHP Shells on wordpress uploaded by Hacker 
[+]  By Mohannad alOtaibi
[+]  Twitter : @ mhnd_it
[+]  GitHub  : Mhndit
|===================================================|\n
'''

if len(sys.argv)<2:
    print "Usage   : wpsniper.py http:// [ Target domain ] / [ wordpress directory ] "
    print "Example : wpsniper.py http://example/blog/"
    sys.exit(1)
	
Tar = sys.argv[1]
TotalShels = ""

def UrlTest(url):
	urlOpen = urllib.urlopen(url)
	UrlCheck = urlOpen.getcode()
	if UrlCheck != 404:
		return True
	else :
		return False

def MhndIt(url):
    soup = BeautifulSoup(requests.get(url).text,"lxml")
    hrefs = []
    for a in soup.find_all('a'):
        hrefs.append(a['href'])
    return hrefs

if UrlTest(Tar) == True :
	print "\n [ + ] connected ! ...."
	fp = open('WpSniper.txt')
	out = fp.read().split("\n")
	for line in out:
		if UrlTest(Tar+line) == True :
			DirList1 = MhndIt(Tar+line)
			for link in DirList1:
				xphp = ['.php','.php3','.phtml']
				for pattern in xphp:
					if re.search(pattern,  link):
						TotalShels+=  " [+] " + Tar + line +link +" \n"
						sys.stdout.write(  " [+] " + Tar + line +link +" \n")
						file = open('result.txt','a')
						file.write("\n [+] " + Tar + line +link)
						sys.stdout.write('\r')
						file.close()
					else :
						sys.stdout.write('\r'+"-[ Not in search "+line+" ]")
						sys.stdout.write('\r')
		else :
			sys.stdout.write('\r'+" [ Scaning ... "+line+" ]")
			sys.stdout.write('\r')
	fp.close()
	sys.stdout.write('\r')
	print "\n\n [ Total files found are : ] "
	print TotalShels
	print "\n + You will find it here : result.txt" 
else :
	print "\b  [ - ] The link is incorrect -> " + Tar + "\n"
	
# @mhnd_it #