import requests,sys,os,time,random
from time import sleep
import random
#note ! jangan recode gan ,cape buatnya hehehe
p = '\x1b[0m'
m = '\x1b[1m'
h = '\x1b[32m'
k = '\x1b[31m'
b = '\x1b[34m'
u = '\x1b[36m'
bm = '\x1b[37m'
bgm = '\x1b[92m'
bgp = '\x1b[93m'
res = '\x1b[94m'
def progress(percent=0, width=30):
	left = width * percent // 100
	right = width - left
	print(b+'\r['+k+'→'+b+'] umay cari sukses [', m+' ↓ ' * left, ' ' * right, b+']'+h,f' {percent:.0f}%',sep='', end='', flush=True)
def load():
	for i in range(101):
	    progress(i)
	    sleep(random.random() * 0.1)
def que():
	logo()
	query = input('\t'+b+'['+k+'?'+b+']'+h+'ip\t\t : '+k)
	outp = input('\t'+b+'['+k+'?'+b+']'+h+'output file\t : '+k)
	if(query=='' or query==' '):
		print(m+'masukan dengan benar')
		que()
	elif(outp=='' or outp==' '):
		print(m+'yg anda masukan salah')
		que()
	else:
		rever(query,outp)
def rever(query,outp):
	logo()
	load()
	a=requests.get('https://api.hackertarget.com/reverseiplookup/?q='+query).text
	jalan(b+'\n['+k+'!'+b+']'+h+' reverse selesai sedang menyimpan hasil')
	si=open(outp,'w')
	si.write(a)
	si.close()
	aw=len(open(outp).readlines())
	print(b+'['+k+'!'+b+']'+h+' %s website tersimpan' % aw)
	jalan(b+'['+k+'!'+b+']'+h+'sukses'+p)
def logo():
	os.system('clear')
	os.system("figlet '            ip reverse'|lolcat")
	print('\n\t'+b+'Author : '+h+'ANAK THEBONG UMAY CARI SUKSES')
def jalan(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)
try:
	que()
except:
	jalan(m+'\nterjadi kesalahan'+p)
