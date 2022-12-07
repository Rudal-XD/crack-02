import requests,bs4,json,os,sys,random,datetime,time,re

import threading

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as parser

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col


id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]



x = '\33[m' # DEFAULT

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

P = '\033[0;00m'

J = '\033[0;33m'

S = '\033[0;00m'

N = '\x1b[0m'

I ='\033[0;32m'

C ='\033[0;36m'

M ='\033[0;31m'

U ='\033[0;35m'

K ='\033[0;33m'

P='\033[00m'

h='\033[0;90m'

Q="\033[00m"

kk='\033[0;32m'

ff='\033[0;36m'

G='\033[0;36m'

p='\033[00m'

h='\033[0;90m'

Q="\033[00m"

I='\033[0;32m'

II='\033[0;36m'

m='\033[0;31m'

O ='\033[0;33m'

H='\033[0;33m'

b = '\033[0;36m'

war = "[•]"

B = random.choice([U,I,K,b,M])



dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}

dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def clear():
	os.system('clear')
def back():
	menu()
def banner():
	print('''%s
	_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
                                                               
───────────────────────────────────────────────────────
 [\x1b[1;96m+%s] Author   : Rudal-XD
 [\x1b[1;96m+%s] Github   : -
 [\x1b[1;96m+%s] Facebook : Fanky
───────────────────────────────────────────────────────\n'''%(N,N,N,N))


balmond = O+"["+J+"•"+O+"]"

class menu:
		def login():
			banner()
			sky = '# MASUKAN TOKEN FACEBOOK'
			sky2 = mark(sky, style='green')
			sol().print(sky2, style='cyan')
			panda = input(x+'['+p+'•'+x+'] Token Fb : ')
			akun=open('.token.x','w').write(panda)
			try:
				tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
				tes3 = json.loads(tes.text)['id']
				sue = '# nice Login berhasil'
				suu = mark(sue, style='green')
				sol().print(suu, style='cyan')
				time.sleep(2)
				menu()
			except KeyError:
				sue = '# Login Gagal, Cek token'
				suu = mark(sue, style='red')
				sol().print(suu, style='cyan')
				time.sleep(2)
				login()
			except requests.exception.ConnectionError:
				li = '# KONEKSI INTERNET 									BERMASALAH, PERIKSA & COBA LAGI'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				menu()
		
if __name__=='__main__':
	menu()
