#Sc Make By Asraful Islam Hasan
#https://github.com/KgHasan
#https://www.facebook.com/copy.link.erorr404

import os,re,sys,bs4,time,json,random,datetime,requests
ses=requests.Session()

FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+" "+str(bln)+" "+str(thn)
os.system('xdg-open https://facebook.com/groups/551365756758487/')
logo = ('''\033[1;97m
          \033[38;5;46m╔═════════════════════════════════════╗
          \033[38;5;196m║\033[38;5;45m<>\033[38;5;192m<>\033[38;5;46m<>\033[38;5;195mWELLCOME HASAN WORLD BRO\033[38;5;45m<>\033[38;5;192m<>\033[38;5;46m<> \033[38;5;196m║
   \033[38;5;192m╔═══════════════════════════════════════════════════╗
   \033[38;5;196m║\033[38;5;46m<>\033[38;5;195mA\033[38;5;45m<>\033[38;5;46m██   ██  █████  ███████  █████  ███    ██\033[38;5;45m<>\033[38;5;195mJ\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║\033[38;5;46m<>\033[38;5;195mD\033[38;5;45m<>\033[38;5;46m██   ██ ██   ██ ██      ██   ██ ████   ██\033[38;5;45m<>\033[38;5;195mA\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║\033[38;5;46m<>\033[38;5;195mM\033[38;5;45m<>\033[38;5;46m███████ ███████ ███████ ███████ ██ ██  ██\033[38;5;45m<>\033[38;5;195mH\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║\033[38;5;46m<>\033[38;5;195mI\033[38;5;45m<>\033[38;5;46m██   ██ ██   ██      ██ ██   ██ ██  ██ ██\033[38;5;45m<>\033[38;5;195mI\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;196m║\033[38;5;46m<>\033[38;5;195mN\033[38;5;45m<>\033[38;5;46m██   ██ ██   ██ ███████ ██   ██ ██   ████\033[38;5;45m<>\033[38;5;195mD\033[38;5;46m<>\033[38;5;196m║
   \033[38;5;192m╚═══════════════════════════════════════════════════╝
   \033[38;5;46m╔═══════════════════════════════════════════════════╗
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mCREATED BY  \033[38;5;46m <\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mK\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191mASRAFUL ISLAM HASAN    \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mFACEBOK      \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mG\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m>\033[38;5;191m Hasa N                 \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mGITHUB       \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mH\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191mKgHasan                \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mTOOL STATUS  \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mA\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m>\033[38;5;191m Fb Bot Share           \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mTEAM         \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mS\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191mKST                    \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mTOOL VIRSION \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mA\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191m02.06                  \033[38;5;196m║
   \033[38;5;196m║ \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mUPDATE TIME  \033[38;5;46m<\033[38;5;192m║\033[38;5;196m<>\033[38;5;45mN\033[38;5;196m<>\033[38;5;192m║\033[38;5;46m> \033[38;5;191mDT-01/4/23 TE-12.30 Am \033[38;5;196m║
   \033[38;5;46m╚═══════════════════════════════════════════════════╝
   \033[38;5;46m╔═══════════════════════════════════════════════════╗
   \033[38;5;196m║\033[38;5;45m<>\033[38;5;192m<>\033[38;5;46m<> \033[38;5;195mPLZ SAPPORT ME BRO....                      \033[38;5;196m║
   \033[38;5;196m║\033[38;5;45m<>\033[38;5;192m<>\033[38;5;46m<> \033[38;5;195mHASAN TERMUX HELPING ZONE....               \033[38;5;196m║
   \033[38;5;46m╚═══════════════════════════════════════════════════╝
''')

def login():
        os.system('clear')
        print (logo)
        print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
        cookie = input('   \033[38;5;192m║\033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m Log In Your Cookie \033[38;5;196m: \033[38;5;46m')
        print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
            token = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(token):
                open('cookie.txt','w').write(cookie)
                open('token.txt','w').write(token)
                print ("\n   \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m Cookie Chaking...")
                bot(cookie)
        except AttributeError:
        	exit("\n   \033[38;5;192m[\033[38;5;45m×\033[38;5;192m] \033[38;5;195m Your Cookie Expired !!")
        except requests.exceptions.ConnectionError:
        	exit("\n   \033[38;5;192m[\033[38;5;45m×\033[38;5;192m] \033[38;5;195m Cannect Your Intarnet Canection !!!")
        

			
def bot(cookie):
	waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
	kuki = cookie
	toket = open("token.txt","r").read()
	respon = random.choice(['Semangat Bang','Keren Bang','Gokil Suhu','Panutanku','Semangat Terus'])
	kom = ("\n\nhttps://www.facebook.com/100089033379675/posts/139149639062815/?app=fbl\n\nKomentar Ini Ditulis Oleh Bot")
	requests.post("https://graph.facebook.com/100089033379675_139149639062815/comments?message=" + respon + ""+ kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+toket,headers = {"cookie":kuki})
	share()
            

def share():
	os.system('clear')
	print (logo)
	header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
	print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
	uiz = input(f"   \033[38;5;192m║\033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m Past Your Post Link: \033[38;5;46m")
	print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
	os.system("clear")
	print(logo)
	print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
	coy = int(input(f"   \033[38;5;192m║\033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m Your Share Limit : \033[38;5;46m"))
	print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
	print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
	print("   \033[38;5;192m║\033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m HASAN POST SHARE TOOLS                        \033[38;5;192m║")
	print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
	print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
	print("   \033[38;5;192m║\033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m Share Start Chake Your Post                   \033[38;5;192m║")
	print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
	print("")
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	try:
		for PahrulXD in range(coy):
			PahrulXD+=1
			ress = ses.post(f"https://graph.facebook.com/me/feed?link={uiz}&published=0&access_token={token}",headers=header, cookies=coki).json()
			if "id" in ress:
				print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
				print ("   \033[38;5;192m║\033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195mSHARE DONE : "+ress['id'])
				print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
				sys.stdout.flush()
			else:
				exit()
		#print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
		print("")
		print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
		print("   \033[38;5;192m║               \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m complate Bro                   \033[38;5;192m║")
		print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
		print("")
		print("   \033[38;5;46m╔═══════════════════════════════════════════════════╗")
		pahrul = input ("   \033[38;5;192m║               \033[38;5;192m[\033[38;5;45m✓\033[38;5;192m] \033[38;5;195m  Back Bro                      \033[38;5;192m║")
		print("   \033[38;5;46m╚═══════════════════════════════════════════════════╝")
		share()
	except requests.exceptions.ConnectionError:
		exit()
		
		
login()
