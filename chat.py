# -*- coding: utf-8 -*-
# Dua,tiga rekode
# Serah ajg

import requests,os,sys,time,json
from bs4 import BeautifulSoup
from tqdm import tqdm
from pyquery import PyQuery
print("\033[0m")
m = "\033[1;91m"
h = "\033[1;92m"
k = "\033[1;93m"
b = "\033[1;96m"
p = "\033[1;97m"
t = "\033[0m"
url = "http://rezadkimx.000webhostapp.com"
res = requests.Session()
welkam = m+" Welcome to DeepCHAT "

def end():
	raw_input(p+"Press Enter ...")

def tik():
    for i in tqdm(range(10)):
	time.sleep(0.1)
	pass

def ceklog():
	global nama,user,gender,alamat,idi
	os.system('clear')
	print("Wait a minute ...")
	try:
		file_json = open('data_login.json')
		de = json.loads(file_json.read())
		isi = {"username_login":de["username_login"], "password_login":de["password_login"], "submit_login":"LOGIN"}
		y = res.post(url+"/chat/index.php", data=isi)
		content = y.text
		q = PyQuery(content)
		nama = q("nama").text()
		user = q("user").text()
		gender = q("gender").text()
		alamat = q("alamat").text()
		idi = q("idi").text()
		if "Login Berhasil" in q("title").text():
			sep = open("data_login.json","w")
			sep.write('{"username_login":"'+de["username_login"]+'", "password_login":"'+de["password_login"]+'"}')
			time.sleep(1)
			menu()
		else:
			print(m+"~ "+p+"Login Failed !")
			time.sleep(1)
			main()
	except (ValueError, IOError):
		main()

def main():
	os.system("clear")
	ser = res.get("https://raw.githubusercontent.com/rezadkim/DeepCHAT/master/server.json")
	sers = json.loads(ser.text)
	print(p+"["+m+welkam+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(h+"> "+p+"Server : "+h+sers["server"])
	print(p+"|"+h+"1"+p+"| Login")
	print(p+"|"+h+"2"+p+"| Register")
	print(p+"|"+h+"3"+p+"| Information")
	print(p+"|"+m+"0"+p+"| Cancel")
	pilih = raw_input("|Choose > ")
	if pilih in ['1','01']:
		login()
	elif pilih in ['2','02']:
		register()
	elif pilih in ['3','03']:
		information()
	elif pilih in ['0','00']:
		exit(m+"Exit ...")
	else:
		main()

def information():
	os.system("clear")
	print(p+"["+m+welkam+p+"]").center(77)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(t+"Author : (ZP) Rezadkim")
	print(t+"Tools name : DeepCHAT")
	print(t+"Version : 0.2")
	print(t+"Source : https://github.com/rezadkim")
	print(t+"Contact : rezaadilhakim2202@gmail.com")
	print(t+"About : this tool is used for small talk with a group of mindless hackers :v")
	print
	end()
	main()

def login():
	global nama,user,gender,alamat,idi
	print
	us = raw_input(h+"> "+p+"Username : ")
	ps = raw_input(h+"> "+p+"Password : ")
	print(h+"%"+p+" Loading ...")
	isi = {"username_login":us, "password_login":ps, "submit_login":"LOGIN"}
	y = res.post(url+"/chat/index.php", data=isi)
	content = y.text
	q = PyQuery(content)
	title = q("title").text()
	nama = q("nama").text()
	user = q("user").text()
	gender = q("gender").text()
	alamat = q("alamat").text()
	idi = q("idi").text()
	if "Login Berhasil" in title:
		print(h+"~ "+p+"Login Success !")
		sep = open("data_login.json","w")
		sep.write('{"username_login":"'+us+'", "password_login":"'+ps+'"}')
		time.sleep(1)
		end()
		menu()
	else:
		print(m+"~ "+p+"Login Failed !")
		time.sleep(1)
		end()
		main()

def register():
	print
	full_name = raw_input(h+"> "+p+"Full Name : ")
	if full_name =="":
		register()
	print(p+"|"+h+"1"+p+"| Male")
	print(p+"|"+h+"2"+p+"| Female")
	kelamin = raw_input("|Choose > ")
	if kelamin in ['1','01']:
		type = '1'
	elif kelamin in ['2','02']:
		type = '2'
	else:
		register()
	country = raw_input(h+"> "+p+"Country : ")
	if country =="":
		register()
	us = raw_input(h+"> "+p+"Username : ")
	if us =="":
		register()
	ps = raw_input(h+"> "+p+"Password : ")
	if ps =="":
		register()
	time.sleep(2)
	isi = {"nama_lengkap_daftar":full_name, "gender_daftar":type, "alamat_daftar":country, "username_daftar":us, "password_daftar":ps}
	y = res.post(url+"/chat/proses_daftar_member.php", data=isi)
	rl = json.loads(y.text)
	if "Pendaftaran Berhasil, Silahkan Login" in rl["teks"]:
		print(h+"~ "+p+"Registration Successful !")
		time.sleep(1)
		print(h+"% "+p+"Save important data ...")
		sep = open("data.json", "w")
		sep.write('{"nama_lengkap_daftar":"'+full_name+'", "gender_daftar":"'+type+'", "alamat_daftar":"'+country+'", "username_daftar":"'+us+'", "password_daftar":"'+ps+'"}')
		sep.close()
		tik()
		print(h+"~ "+p+"Success : "+h+"data.json")
		raw_input(h+">> "+p+"[Press Enter to back menu]")
		main()
	else:
		print(m+"~ "+p+"Registration Failed !")
		time.sleep(1)
		end()
		main()

def menu():
	nau = time.ctime()
	ser = res.get("https://raw.githubusercontent.com/rezadkim/DeepCHAT/master/server.json")
	sers = json.loads(ser.text)
	if "L" in gender:
		kel = "Male"
	else:
		kel = "Female"
	y = res.get(url+"/chat/index.php")
	content = y.text
	q = PyQuery(content)
	total = q("total").text()
	os.system("clear")
	print(p+"["+m+welkam+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(h+"> "+p+"Server : "+h+sers["server"]+h+"  | "+p+"Now : "+nau)
	print(h+"# "+p+nama+" : "+h+"Online  "+h+"| "+p+"Your ID : "+idi)
	print(h+"# "+p+"Username : "+user)
	print(h+"# "+p+"Gender : "+kel)
	print(h+"# "+p+"Country : "+alamat)
	print(h+49*"-").center(50)
	print(p+"|"+h+"1"+p+"| Public Chat")
	print(p+"|"+h+"2"+p+"| Open Inbox ("+h+total+p+")")
	print(p+"|"+h+"3"+p+"| Send Message")
	print(p+"|"+m+"0"+p+"| LogOut Account")
	print(p+"|"+m+"x"+p+"| Exit the program")
	zeyeng = raw_input("|Choose > ")
	if zeyeng in ['1','01']:
		pup = m+" Publik Chat "
		os.system("clear")
		print(p+"["+m+welkam+p+"]").center(77)
		print("https://github.com/rezadkim").center(50)
		print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
		print(h+49*"-").center(50)
		print(p+"["+m+pup+p+"]").center(77)
		print("[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
		print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
		print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
		raw_input(h+"Press ENTER to join ...")
		publik()
	elif zeyeng in ['2','02']:
		op_inbox()
	elif zeyeng in ['3','03']:
		senmes()
	elif zeyeng in ['0','00']:
		pek = res.get("http://rezadkimx.000webhostapp.com/chat/dasbor/logout.php")
		os.system("rm -rf data_login.json")
		os.system("rm -rf data.json")
		main()
	elif zeyeng in ['x']:
		exit(m+"Byeee !")
	else:
		menu()

################# Kenthoood
def publik():
	pup = m+" Publik Chat "
	os.system("clear")
	print(p+"["+m+welkam+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"["+m+pup+p+"]").center(77)
	print("[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
	print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
	print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
	os.system('curl '+url+'/publik/index.php')
	zedd = open('publik.txt', 'w')
	zedd.write(b+nama+" Joined ...\n")
	zedd.close()
	myfile = 'publik.txt'
	files = {'upl' : open(myfile, 'r')}
	sen = res.post(url+"/publik/server.php", files = files)
	dat = json.loads(sen.text)
	if "success" in dat['status']:
		msg()
	else:
		print(m+"Error ...")
		exit()

def msg():
	pesan = raw_input(p+"\nType : ")
	if pesan =="clear":
		pup = m+" Publik Chat "
		os.system("clear")
		print(p+"["+m+welkam+p+"]").center(77)
		print("https://github.com/rezadkim").center(50)
		print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
		print(h+49*"-").center(50)
		print(p+"["+m+pup+p+"]").center(77)
		print("[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
		print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
		print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
		msg()
	elif pesan =="exit":
		print(b+nama+m+" Left ...\n")
		zedd = open('publik.txt', 'w')
		zedd.write(b+nama+m+" Left ...\n")
		zedd.close()
		myfile = 'publik.txt'
		files = {'upl' : open(myfile, 'r')}
		sen = res.post(url+"/publik/server.php", files = files)
		dat = json.loads(sen.text)
		if "success" in dat['status']:
			menu()
		else:
			print(m+"Error ...")
			exit()
	elif pesan =="":
		pup = m+" Publik Chat "
		os.system("clear")
		print(p+"["+m+welkam+p+"]").center(77)
		print("https://github.com/rezadkim").center(50)
		print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
		print(h+49*"-").center(50)
		print(p+"["+m+pup+p+"]").center(77)
		print("[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
		print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
		print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
		os.system('curl '+url+'/publik/index.php')
		msg()
	else:
		zs = open('publik.txt', 'w')
		zs.write(p+nama+" : "+pesan+"\n")
		zs.close()
		myfile = 'publik.txt'
		files = {'upl' : open(myfile, 'r')}
		sen = res.post(url+"/publik/server.php", files = files)
		dat = json.loads(sen.text)
		if "success" in dat['status']:
			kirim()
		else:
			print(m+"Error ...")
			exit()

def kirim():
	pup = m+" Publik Chat "
	os.system("clear")
	print(p+"["+m+welkam+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"["+m+pup+p+"]").center(77)
	print("[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
	print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
	print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
	os.system('curl '+url+'/publik/index.php')
	msg()

def op_inbox():
	pup = m+" My INBOX "
	os.system("clear")
	print(p+"["+m+welkam+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"["+m+pup+p+"]").center(77)
	print("[ "+b+"?"+p+" ] Type '"+h+"balas"+p+"' or '"+h+"Reply"+p+"' = reply to the inbox")
	print("[ "+b+"?"+p+" ] Type '"+h+"back"+p+"' = Back to menu")
	hal = res.get('http://rezadkimx.000webhostapp.com/chat/dasbor/pesan.php?id_member='+idi)
	soup = BeautifulSoup(hal.text, 'html.parser')
	sult = soup.find('tbody', id="ajg")
	print sult.text
	bal = raw_input(p+"\nType : ")
	if bal =="":
		op_inbox()
	elif bal =="balas":
		id_send = raw_input(p+"Enter destination ID : ")
		if id_send =="":
			op_inbox()
		else:
			ms = raw_input(p+"Message : ")
			if ms =="":
				op_inbox()
			else:
				isi = {"pengirim_balas_pesan":idi, "penerima_balas_pesan":id_send, "subyek_balas_pesan":nama, "isi_balas_pesan":ms}
				gas = res.post("http://rezadkimx.000webhostapp.com/chat/dasbor/proses_balas_pesan.php", data=isi)
				nof = json.loads(gas.text)
				if "Pesan sudah berhasil terbalas" in nof["teks"]:
					print(h+"~ "+p+"Message successfully answered !")
				else:
					print(m+"~ "+p+"Message failed to reply !")
					time.sleep(1)
	elif bal =="reply":
		id_send = raw_input(p+"Enter destination ID : ")
		if id_send =="":
			op_inbox()
		else:
			ms = raw_input(p+"Message : ")
			if ms =="":
				op_inbox()
			else:
				isi = {"pengirim_balas_pesan":idi, "penerima_balas_pesan":id_send, "subyek_balas_pesan":nama, "isi_balas_pesan":ms}
				gas = res.post("http://rezadkimx.000webhostapp.com/chat/dasbor/proses_balas_pesan.php", data=isi)
				nof = json.loads(gas.text)
				if "Pesan sudah berhasil terbalas" in nof["teks"]:
					print(h+"~ "+p+"Message successfully answered !")
					end()
					menu()
				else:
					print(m+"~ "+p+"Message failed to reply !")
					time.sleep(1)
					end()
					menu()
	elif bal =="back":
		end()
		res.get("http://rezadkimx.000webhostapp.com/chat/dasbor/pesan.php")
		menu()
	else:
		op_inbox()

def senmes():
	pup = m+" Send Message "
	os.system("clear")
	print(p+"["+m+welkam+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"["+m+pup+p+"]").center(77)
	idp = raw_input(p+"Enter recipient ID : ")
	if idp =="":
		senmes()
	else:
		mess = raw_input(p+"Message : ")
		if mess =="":
			senmes()
		else:
			isi = {"pengirim_kirim_pesan":idi, "penerima_kirim_pesan":idp, "subyek_kirim_pesan":nama, "isi_kirim_pesan":mess}
			gas = res.post("http://rezadkimx.000webhostapp.com/chat/dasbor/proses_kirim_pesan.php", data=isi)
			nof = json.loads(gas.text)
			if "Pesan sudah berhasil terkirim" in nof["teks"]:
				print(h+"~ "+p+"Message sent successfully !")
				end()
				menu()
			else:
				print(m+"~ "+p+"Message failed to send !")
				time.sleep(1)
				end()
				menu()




if __name__ == '__main__':
	try:
		ceklog()
	except KeyboardInterrupt:
		exit(m+"\nStopped ...")
