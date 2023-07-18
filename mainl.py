# (c) 2022-2023, adrhmdlz All rights reserved

# 0 - Startup
## 0.1 - Template
def template():
    print(f"Diperbarui pada {last_modified_date}")
    print(f"Author  : Adrian Ahmad Al Zidan")
    print(f"Github  : https://github.com/adrhmdlz")
    print(f"Bahasa  : Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"Waktu	: {waktu_sekarang}")
    print(f"(c) 2021-2022, adrhmdlz All rights reserved")
    print(f"{'-'*45}")

# 1 - Module
from datetime import datetime as dt
from getpass import getpass as gp
import subprocess as sp
import os, sys, time
import os.path

# 2 - Data
## 2.1 - membuat variable yang mengambil data kapan kode nya dimodifkasi
last_modified = os.path.getmtime(__file__)
last_modified_date = time.strftime("%d-%m-%y %H:%M", time.localtime(last_modified))
## 2.2 - membuat sebuah variable yang fungsinya untuk membersihkan terminal
clear = lambda : os.system("clear")
## 2.3 - membuat variable yang berfungsi mengambil data waktu terkini
now = dt.now()
waktu_sekarang = now.strftime("%A, %d %b %Y (%H:%M:%S)")
## 2.4 - membuat list kosong yang nantinya berisi nama user dan ditampilkan pada program
name = []
## 2.5 - membuat dictionary untuk kode pesan output
message = {
	"message_p":"[!]",
	"message_i":"[~]",
	"message_o":"[$]",
	"message_m":"[>]",
	"message_q":"[?]"
	}
## 2.6 - membuat variable nama program
tb = "Tebak-tebakan"
qzz = "Quiz"
rf = "Rekomendasi Film Untuk Mu"
k = "Kalkulator"
## 2.7 - membuat list yang berisikan jawaban untuk program tebak-tebakan
tbk_jwb = ["pohuan maharani", "sepatula", "cap cay", "telortoar", "selena gowes"]
tbk_alt_jwb = ["puan maharani", "spatula", "capcay", "terotoar", "selena gomes"]
## 2.8 - membuat list yang berisikan jawaban untuk program quiz
q_jwb = ["di tv", "1009", "tukang gali kubur", "1 orang", "david"]
q_alt_jwb = ["ditv", "1009", "kang gali kubur", "1", "david"]
## 2.9 - membuat list yang berisi nama film untuk program rfum
film_action = ["Avengers", "Tenet", "Transformers", "The Expendable", "Fast & Furious", "Pacific Rim", "Nobody", "Jurrasic World", "Justice League", "Mortal Kombat"]
film_romance = ["500 Days of Summer", "10 Things I hate About You", "Mr. and Mrs Smith", "Paper Towns", "The Fault in Our Stars", "Kimi No Nawa", "Friends With Benefits", "Pride and Prejudice", "Cinderlla", "Beauty and The Beast"]
film_horror = ["The Medium", "The Counjuring", "The Insidious", "A Quiet Place", "Mata Batin", "The Tall Grass", "Bird Box", "The Curse of La Llorona", "Sabrina", "Impetigore"]
film_comedy = ["Red Notice", "Deadpool", "Free Guy", "Kungfu Hustle", "Jumanji", "My Stupid Bos", "Yowis Ben", "Reuni Z", "The Guys", "Susah Sinyal"]
film_scifi = ["Spider-Man", "Iron-Man", "Venom", "Godzilla", "Terminator", "Evangelion", "Prometheus", "Alien: Covenant", "Captain America", "2012"]

# 3 - Main Program 
## 3.0 - Restart program
def restart_program():
    python = sys.executable
    sp.call([python] + sys.argv)

## 3.1 - Mulai dari sini
def main():
    clear()
    main_banner()
    template()
    response = input(f"{message['message_i']} Tekan enter untuk melanjutkan...")
    user_login_confirmation()

## 3.2 - Konfirmasi user register & login (user akan melakukan register jika belum memiliki akun dan login jika memiliki akun)
def user_login_confirmation():
	clear()
	print(f"{message['message_p']} Sebelum mulai ada baiknya kamu login atau register terlebih dahulu ya")
	while True:
		response = input(f"{message['message_q']} Apakah kamu sudah memiliki akun? (y/n) ")
		if response.lower() == "y":
			time.sleep(1.5)
			user_login() # user akan dibawa ke fungsi login
		elif response.lower() == "n":
			time.sleep(1.5)
			user_register() # user akan dibawa ke fungsi register untuk mendaftarkan nama dan password baru
		else:
			print(f"{message['message_p']} Input yang dimasukan salah")
			time.sleep(1)

## 3.3 - User Login
def user_login():
	clear()
	print(f"{message['message_p']} Silahkan masukan username dan password yang sudah didaftarkan")
	usr_lgn = input("Username : ")
	name.append(usr_lgn)
	passwd_lgn = gp("Password : ")
    # membuka file user.txt
	with open("user.txt", "r") as u:
		user = [line.strip() for line in u]
    # membuka file password.txt
	with open("password.txt", "r") as p:
		passw = [line.strip() for line in p]
	# fungsi dibawah adalah menentukan jika user dan login benar, password salah, dan user tidak terdaftar
	while True:
		# user password benar
		if usr_lgn in user and passwd_lgn in passw:
			time.sleep(2)
			loading()
		# password salah
		elif usr_lgn in user and passwd_lgn not in passw:
			print(f"{message['message_p']} Password yang dimasukan salah")
			time.sleep(1)
			user_login()
		# user tidak terdaftar di data
		else:
			print(f"{message['message_p']} Username {usr_lgn} tidak ada di data")
			time.sleep(1)
			user_login()

## 3.4 - User Register
def user_register():
	clear()
	print(f"{message['message_p']} Silahkan daftar dahulu")
	response1 = input("Masukkan nama yang ingin didaftarkan: ")
	### cek apakah user yang didaftar kan sudah ada atau belum
	with open("user.txt", "r") as u:
		user = [line.strip() for line in u]
	if response1 in user:
		print(f"Data sudah ada, silahkan coba lagi")
		time.sleep(1)
		user_register()
	response2 = gp("Masukkan password yang ingin dipakai: ")
	with open("user.txt", "a") as u:
		u.write(response1 + "\n")
	with open("password.txt", "a") as p:
		p.write(response2 + "\n")
	time.sleep(1.5)
	clear()
	user_login()
    
## 3.5 - Loading
def loading():
	clear()
	n = 100
	for i in range(n):
		time.sleep(0.05)
		sys.stdout.write("\r"+"Loading... Process "+str(i).format(n*100)+"%")
	clear()
	sys.stdout.write("\r"+"Loading... Finished\n")
	print(f"Selamat datang, {name[0]}")
	time.sleep(2)
	main_menu()

## 3.6 - Menu utama
def main_menu():
	clear()
	main_banner()
	template()
	print(f"{message['message_o']} Opsi : ")
	print(f"1. Tebak-tebakan")
	print(f"2. Quiz")
	print(f"3. Rekomendasi Film Untuk Mu")
	print(f"4. Kalkulator Sederhana")
	print(f"5. Check Score Game Kamu")
	print(f"8. About Me")
	print(f"9. Restart Program")
	print(f"0. Keluar Program")
	opsi = input(f"{message['message_c']} Pilihanmu : ")
	while True:
		if opsi == "1":
			time.sleep(1)
			tebak_tebakan()
		elif opsi == "2":
			time.sleep(1)
			quiz()
		elif opsi == "3":
			time.sleep(1)
			rekomen_film()
		elif opsi == "4":
			time.sleep(1)
			kalkulator()
		elif opsi == "5":
			time.sleep(1)
			check_score()
		elif opsi == "8":
			time.sleep(1)
			about_me()
		elif opsi == "9":
			time.sleep(1)
			restart_program()
		elif opsi == "0":
			clear()
			print(f"{message['message_p']} Selamat tinggal, {name[0]}!")
			time.sleep(1.5)
			exit()
		else:
			print(f"{message['message_p']} Error : Input yang dimasukan tidak ada, silahkan pilih input yang lain")
			time.sleep(0.5)

## 3.7 - Tebak-tebakan
def tebak_tebakan():
	clear()
	tebak_tebakan_banner()
	print(f"waktu_sekarang   : {waktu_sekarang}")
	response = input(f"{message['message_p']} Selamat datang di program {tb}, silahkan tekan enter untuk melanjutkan...")
	time.sleep(1.5)
	tebak_tebakan_main()
### 3.7.1 - Mulai Game
def tebak_tebakan_main():
	clear()
	tbkscore = 0
	soal = 1
	#### 3.7.1.1 - Soal nomor 1
	print(f"{message['message_q']} {soal}. Pohon pohon apa yang ditakuti negara? (hint : dpr)")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == tbk_jwb[0] or tbk_alt_jwb[0]:
		time.sleep(1)
		tbkscore = tbkscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{tbk_jwb[0]}'. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.7.1.2 - Soal nomor 2
	print(f"{message['message_q']} {soal}. Sepatu, sepatu apa yang bisa dibuat masak? (hint : patty)")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == tbk_jwb[1] or tbk_alt_jwb[1]:
		time.sleep(1)
		tbkscore = tbkscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{tbk_jwb[1]}'. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.7.1.3 - Soal nomor 3
	print(f"{message['message_q']} {soal}. Bahasa mandarinnya aneka macam sayur? (hint : aplikasi edit jj)")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == tbk_jwb[2] or tbk_alt_jwb[2]:
		time.sleep(1)
		tbkscore = tbkscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{tbk_jwb[2]}'. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.7.1.4 - Soal nomor 4
	print(f"{message['message_q']} {soal}. Telor, telor apa yang diinjek tapi ngga pecah? (hint : jembatan)")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == tbk_jwb[3] or tbk_alt_jwb[3]:
		time.sleep(1)
		tbkscore = tbkscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{tbk_jwb[3]}'. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.7.1.5 - Soal nomor 5
	print(f"{message['message_q']} {soal}. Siapa nama penyanyi yang suka naik sepeda? (hint : cwk)")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == tbk_jwb[4] or tbk_alt_jwb[4]:
		time.sleep(1)
		tbkscore = tbkscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{tbk_jwb[4]}'. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	### 3.7.2 - Game selesai, memprint hasil score
	print(f"Yeay, kamu telah menyelesaikan game {tb} ini. Silahkan lihat hasil score yang kamu dapatkan dibawah")
	print(f"Score : {tbkscore}/{(soal*2)-2}")
	while True:
		response = input(f"{message['message_q']} Apakah kamu ingin kembali ke menu utama? (y/n) ")
		if response.lower() == "y":
			time.sleep(1.5)
			return tbkscore
			main_menu()
		elif response.lower() == "n":
			clear()
			print(f"{message['message_p']} Selamat tinggal, {name[0]}")
			time.sleep(1.5)
			exit()
		else:
			print(f"{message['message_p']} Error : Input yang dimasukan tidak ada, silahkan coba lagi")
			time.sleep(1)

## 3.8 - Quiz
def quiz():
	clear()
	quiz_banner()
	print(f"waktu_sekarang   : {waktu_sekarang}")
	response = input(f"{message['message_p']} Selamat datang di program {qzz}, silahkan tekan enter untuk melanjutkan...")
	time.sleep(1.5)
	quiz_main()
### 3.8.1 - Mulai Game
def quiz_main():
	clear()
	qscore = 0
	soal = 1
	#### 3.8.1.1 - Soal nomor 1
	print(f"{message['message_q']} {soal}. Kalau ada bus kecelakaan, pesawat jatuh, ada kapal tenggelam, semuanya akan muncul di mana?")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == q_jwb[0] or q_alt_jwb[0]:
		time.sleep(1)
		qscore = qscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{q_jwb[0]}'. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.8.1.2 - Soal nomor 2
	print(f"{message['message_q']} {soal}. Jika ada 10 pejuang Indonesia yang berestart_programerang lalu ada satu orang yang gugur, ada berapa orang yang akan kembali ke markas?")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == q_jwb[1] or q_alt_jwb[1]:
		time.sleep(1)
		qscore = qscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{q_jwb[1]}'. Karena pepatah mengatakan 'mati 1 tumbuh 1000', hehehe. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.8.1.3 - Soal nomor 3
	print(f"{message['message_q']} {soal}. Kalau gajah mati siapa yang paling sedih?")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == q_jwb[2] or q_alt_jwb[2]:
		time.sleep(1)
		qscore = qscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{q_jwb[2]}'. Soalnya diperlukan lobang yang besar untuk mengguburkan gajah, hehehe. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.8.1.4 - Soal nomor 4
	print(f"{message['message_q']} {soal}. Dalam sebuah keluarga, terdapat 3 anak perempuan yang masing-masing memiliki 1 adik laki-laki. Berapakah jumlah anak laki-laki dalam keluarga tersebut?")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == q_jwb[3] or q_alt_jwb[3]:
		time.sleep(1)
		qscore = qscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{q_jwb[3]}'. Soalnya adik laki-laki dari anak perempuan yang satu adalah adik laki-laki dari anak perempuan lainnya, hehehe. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	#### 3.8.1.5 - Soal nomor 5
	print(f"{message['message_q']} {soal}. Ibu david punya anak 4, jona, joni, jeni. Siapakah nama anak ke 4?")
	response = input(f"{message['message_c']} Jawabanmu : ")
	if response.lower() == q_jwb[4] or q_alt_jwb[4]:
		time.sleep(1)
		qscore = qscore + 2
		soal = soal + 1
	else:
		print(f"{message['message_i']} Salah, yang benar adalah '{q_jwb[4]}'. Kan ibu david punya anak 4, jona joni jeni yang terakhir berarti david dong, hadehh. Maav, kamu kurang beruntung :(")
		time.sleep(1)
	### 3.8.2 - Game berakhir, memprint hasil score
	print(f"Yeay, kamu telah menyelesaikan game {qzz} ini. Silahkan lihat hasil score yang kamu dapatkan dibawah")
	print(f"Score : {qscore}/{(soal*2)-2}")
	while True:
		response = input(f"{message['message_q']} Apakah kamu ingin kembali ke menu utama? (y/n) ")
		if response.lower() == "y":
			time.sleep(1.5)
			return qscore
			main_menu()
		elif response.lower() == "n":
			clear()
			print(f"{message['message_p']} Selamat tinggal, {name[0]}")
			time.sleep(1.5)
			exit()
		else:
			print(f"{message['message_p']} Error : Input yang dimasukan tidak ada, silahkan coba lagi")
			time.sleep(1)

## 3.9 - Rekomendasi Film Untuk Mu
def rekomen_film():
	clear()
	rekomen_film_banner()
	print(f"waktu_sekarang   : {waktu_sekarang}")
	response = input(f"{message['message_p']} Selamat datang di program {rf}, silahkan tekan enter untuk melanjutkan...")
	time.sleep(1.5)
	rekomen_film_main()
### 3.9.1 - Mulai
def rekomen_film_main():
	print(f"{message['message_p']} Silahkan pilih genre yang kalian suka : (a)ction/(r)omance/(h)orror/(c)omedy/(s)cifi/(e)xit")
	response = input(f"{message['message_c']} Pilihanmu : ")
	while True:
		#### 3.9.1.1 - Pilihan untuk rekomendasi film Action
		if response.lower() == "a":
			nmr = 1
			print(f"Pilihan film yang bagus untuk mu adalah :")
			for i in film_action:
				print(f"{nmr}. {i}")
				nmr = nmr + 1
			
			response = input(f"{message['message_q']} Apakah ingin mencari rekomendasi lain? (y/n) ")
			while True:
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekomen_film_main()
				elif response.lower() == "n":
					time.sleep(1)
					main_menu()
				else:
					print(f"{message['message_p']} Input tidak dikenali")
		#### 3.9.1.2 - Pilihan untuk rekomendasi film Romance
		elif response.lower() == "r":
			nmr = 1
			print(f"Pilihan film yang bagus untuk mu adalah :")
			for i in film_romance:
				print(f"{nmr}. {i}")
				nmr = nmr + 1
			
			response = input(f"{message['message_q']} Apakah ingin mencari rekomendasi lain? (y/n) ")
			while True:
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekomen_film_main()
				elif response.lower() == "n":
					time.sleep(1)
					main_menu()
				else:
					print(f"{message['message_p']} Input tidak dikenali")
		#### 3.9.1.3 - Pilihan untuk rekomendasi film Horror
		elif response.lower() == "h":
			nmr = 1
			print(f"Pilihan film yang bagus untuk mu adalah :")
			for i in film_horror:
				print(f"{nmr}. {i}")
				nmr = nmr + 1
			
			response = input(f"{message['message_q']} Apakah ingin mencari rekomendasi lain? (y/n) ")
			while True:
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekomen_film_main()
				elif response.lower() == "n":
					time.sleep(1)
					main_menu()
				else:
					print(f"{message['message_p']} Input tidak dikenali")
		#### 3.9.1.4 - Pilihan untuk rekomendasi film Comedy
		elif response.lower() == "c":
			nmr = 1
			print(f"Pilihan film yang bagus untuk mu adalah :")
			for i in film_comedy:
				print(f"{nmr}. {i}")
				nmr = nmr + 1
			
			response = input(f"{message['message_q']} Apakah ingin mencari rekomendasi lain? (y/n) ")
			while True:
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekomen_film_main()
				elif response.lower() == "n":
					time.sleep(1)
					main_menu()
				else:
					print(f"{message['message_p']} Input tidak dikenali")
		#### 3.9.1.5 - Pilihan untuk rekomendasi film Sci-Fi
		elif response.lower() == "s":
			nmr = 1
			print(f"Pilihan film yang bagus untuk mu adalah :")
			for i in film_scifi:
				print(f"{nmr}. {i}")
				nmr = nmr + 1
			
			response = input(f"{message['message_q']} Apakah ingin mencari rekomendasi lain? (y/n) ")
			while True:
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekomen_film_main()
				elif response.lower() == "n":
					time.sleep(1)
					main_menu()
				else:
					print(f"{message['message_p']} Input tidak dikenali")
		elif response.lower() == "e":
			clear()
			print(f"{message['message_p']} Selamat tinggal, {name[0]}")
			time.sleep(1.5)
			exit()
		else:
			print(f"{message['message_p']} Error : Input yang dimasukan tidak ada, silahkan coba lagi")
			time.sleep(1)

## 3.10 - Kalkulator
def kalkulator():
	clear()
	kalkulator_banner()
	print(f"waktu_sekarang   : {waktu_sekarang}")
	response = input(f"{message['message_p']} Selamat datang di program {k}, silahkan tekan enter untuk melanjutkan...")

## 3.11 - Check Score
def check_score():
	pass

## 3.12 - About Me
def about_me():
    pass

# 4 - Banner
## 4.1 - Start Banner
def main_banner():
	print(f'                   _         _    ')
	print(f'                  | |       | |   ')
	print(f'  __ _ _ __  _ __ | | _____ | | __')
	print(f' / _` | \'_ \\| \'_ \\| |/ / _ \\| |/ /')
	print(f'| (_| | |_) | |_) |   < (_) |   < ')
	print(f' \\__, | .__/| .__/|_|\\_\\___/|_|\\_\\ ')
	print(f'  __/ | |   | |__________________ ')
	print(f' |___/|_|   |____________________|\n')
## 4.2 - Tebak-tebakan banner
def tebak_tebakan_banner():
	print(' _   _     _    _   _     _               ')
	print('| | | |   | |  | | | |   | |              ')
	print('| |_| |__ | | _| |_| |__ | | ____ _ _ __  ')
	print('| __| \'_ \\| |/ / __| \'_ \\| |/ / _` | \'_ \\ ')
	print('| |_| |_) |   <| |_| |_) |   < (_| | | | |')
	print(' \\__|_.__/|_|\\_\\\\__|_.__/|_|\\_\\__,_|_| |_|')
	print('-------------------------------------------')
## 4.3 - Quiz banner
def quiz_banner():
	print('             _     ')
	print('            (_)    ')
	print('  __ _ _   _ _ ____')
	print(' / _` | | | | |_  /')
	print('| (_| | |_| | |/ / ')
	print(' \\__, |\\__,_|_/___|')
	print('    | |            ')
	print('    |_|            ')
	print('-------------------')
## 4.4 - Rekomendasi Film Untuk Mu
def rekomen_film_banner():
	print('       __                 ')
	print('      / _|                ')
	print(' _ __| |_ _   _ _ __ ___  ')
	print('| \'__|  _| | | | \'_ ` _ \ ')
	print('| |  | | | |_| | | | | | |')
	print('|_|  |_|  \__,_|_| |_| |_|')
	print('--------------------------')
## 4.5 - Kalkulator Sederhana
def kalkulator_banner():
	print(' _  __     _ _          _       _             ')
	print('| |/ /    | | |        | |     | |            ')
	print('| \' / __ _| | | ___   _| | __ _| |_ ___  _ __ ')
	print('|  < / _` | | |/ / | | | |/ _` | __/ _ \| \'__|')
	print('| . \ (_| | |   <| |_| | | (_| | || (_) | |   ')
	print('|_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|   ')
	print('----------------------------------------------')

# 5 - Program Execution
try:
	if __name__ == "__main__":
		main()
except KeyboardInterrupt:
	print(f"\n{message['message_p']} CTRL + C detected, exiting program...")
	time.sleep(1.5)
	exit()