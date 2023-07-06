# encoding: utf-8
# (c) 2021-2022, yn All rights reserved

# 1 - Import module
from datetime import datetime as dt
import time, os, sys


# 2 - Data, list, etc
usr = []
aby = []
now = dt.now()
waktu = now.strftime("%A, %d %b %Y (%H:%M:%S)")
clear = lambda : os.system("clear")


# 3 - Menu, Function, etc
# 3.1 - Restart program
def restart_program():
	time.sleep(1)
	start()

# 3.2 - Start menu
def start():
	clear()
	b1()
	try:
		print("Diperbarui pada 25-12-2021 (00:06)")
		print("Author		: yn")
		print("Github 		: https://github.com/myynxlazz")
		print("Bahasa		: Python versi 3")
		print("Deskripsi	: Just for fun")
		enter = input("[~] Tekan Enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	except EOFError:
		print('\n[!] Error : CTRL + D Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	user()

# 3.3 - Ask for name
def user():
	name = str(input("How do i call you? : "))
	if name.lower() == "fazila":
		usr.append(name)
		bd = "22 Agustus 2004"
		aby.append(bd)
		tl = "Malang"
		aby.append(tl)
		ns = "SMK Telkom Malang"
		aby.append(ns)
		nj = "RPL"
		aby.append(nj)
		np = "adrian"
		aby.append(np)
		time.sleep(2)
		loading()
	elif name.lower() == "":
		alt_name = "Catfish"
		response = input(f"Kalo aku panggil kamu {alt_name}, boleh ga? (y/n) ")
		if response.lower() == "y":
			name = alt_name
			usr.append(name)
			print(f"Asikk, mulai sekarang aku panggil kamu {name}")
			time.sleep(2)
			loading()
		elif response.lower() == "n":
			print("Ah kamu ga asik :(")
			time.sleep(2)
			clear()
			user()
		else:
			print(f"Yahh, gajelas nih. Yaudah kamu aku panggil {alt_name} aja")
			name = alt_name
			usr.append(name)
			time.sleep(2)
			loading()

# 3.4 - Loading screen
def loading():
	clear()
	n = 100
	for i in range(n):
		time.sleep(0.05)
		sys.stdout.write("\r"+"Loading... Process "+str(i).format(n*100)+"%")
	clear()
	sys.stdout.write("\r"+"Loading... Finished\n")
	print("Selamat datang,", usr[0])
	time.sleep(2)
	clear()
	b1()
	menu()

# 3.5 - Menu
def menu():
	print("Diperbarui pada 25-12-2021 (00:06)")
	print("Author		: yn")
	print("Github 		: https://github.com/myynxlazz")
	print("Bahasa		: Python versi 3")
	print("Versi		: 1.3")
	print(f"Time Now	: {waktu}", end="/r")
	print("(c) 2021-2022, yn All rights reserved")
	print("-------------------------------------")
	print("[$] Opsi :")
	print("	1. Tebak-tebakan")
	print("	2. Quiz")
	print("	3. Rekomendasi Film Untuk Mu")
	print("	8. About me")
	print("	9. Restart Program")
	print("	0. Keluar Program")
	try:
		opsi = input("[>] Pilihanmu : ")
		while True:
			if opsi == "1":
				time.sleep(1)
				tbk()
			elif opsi == "2":
				time.sleep(1)
				qz()
			elif opsi == "3":
				time.sleep(1)
				rfum()
			elif opsi == "8":
				time.sleep(1)
				abt()
			elif opsi == "9":
				clear()
				time.sleep(1)
				restart_program()
			elif opsi == "0":
				clear()
				print("[!] Selamat tinggal, dadah :)")
				time.sleep(2)
				exit()
			else:
				print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
				time.sleep(1)
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	except EOFError:
		print('\n[!] Error : CTRL + D Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()

# 3.6 - Tebak-tebakan
def tbk():
	clear()
	b2()
	try:
		print(f"Time Now 	: {waktu}")
		tb = input("\nSelamat datang di game Tebak-tebakan, silahkan tekan enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	except EOFError:
		print('\n[!] Error : CTRL + D Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	tb1()
# 3.6.1 - Pertanyaan
def tb1():
	tbkscore = 0
	print("1. Pohon pohon apa yang ditakuti negara? (hint : nikah)")
	response = input("Jawaban mu : ")
	if response.lower() == "pohuan maharani":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"pohuan maharani\".\nChuaakkks. Maav, kamu kurang beruntung...\n\n")
		time.sleep(1)

	print("2. Sepatu, sepatu apa yang bisa dibuat masak? (hint : bikini bottom)")
	response = input("Jawaban mu : ")
	if response.lower() == "sepatula":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"sepatula\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("3. Bahasa mandarinnya aneka macam sayur? (hint : edit video)")
	response = input("Jawaban mu : ")
	if response.lower() == "cap cay":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"cap cay\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("4. Telor, telor apa yang diinjek tapi ngga pecah? (hint : jalan raya)")
	response = input("Jawaban mu : ")
	if response.lower() == "telortoar":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"telortoar\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("5. Siapa nama penyanyi yang suka naik sepeda? (hint : cwk)")
	response = input("Jawaban mu : ")
	if response.lower() == "selena gowes":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"selena gowes\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1) 
		
	print("Yeay, kamu sudah menyelesaikan permainan Tebak-tebakan ini. Ditunggu ya update berikutnya! :)")
	print("Berikut score yang berhasil kamu proleh : ", tbkscore, "/ 10\n\n")
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.7 - Quiz
def qz():
	clear()
	b3()
	try:
		print(f"Time Now	: {waktu}")
		tb = input("\nSelamat datang di game Quiz, silahkan tekan enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	except EOFError:
		print('\n[!] Error : CTRL + D Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	qz1()
# 3.7.1 - Pertanyaan quiz
def qz1():
	qzscore = 0
	print("1. Kalau ada bus kecelakaan, pesawat jatuh, ada kapal tenggelam, semuanya akan muncul di mana?")
	response = input("Jawabanmu : ")
	if response.lower() == "di tv":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"di tv\". Maav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("2. Jika ada 10 pejuang Indonesia yang berperang lalu ada satu orang yang gugur, ada berapa orang yang akan kembali ke markas?")
	response = input("Jawabanmu : ")
	if response.lower() == "1009":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"1009\". Karena pepatah mengatakan \"mati 1 tumbuh 1000\", hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("3. Kalau gajah mati siapa yang paling sedih?")
	response = input("Jawabanmu : ")
	if response.lower() == "tukang gali kubur":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"tukang gali kubur\". Soalnya diperlukan lobang yang besar untuk mengguburkan gajah, hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("4. Dalam sebuah keluarga, terdapat 3 anak perempuan yang masing-masing memiliki 1 adik laki-laki. Berapakah jumlah anak laki-laki dalam keluarga tersebut?")
	response = input("Jawabanmu : ")
	if response.lower() == "1 orang":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"1 orang\". Soalnya adik laki-laki dari anak perempuan yang satu adalah adik laki-laki dari anak perempuan lainnya, hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("5. Ibu david punya anak 4, jona, joni, jeni. Siapakah nama anak ke 4?")
	response = input("Jawabanmu : ")
	if response.lower() == "david":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"david\". Kan ibu david punya anak 4, jona joni jeni yang terakhir berarti david dong, hadehh.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("Yeay, kamu sudah menyelesaikan permainan Quiz ini. Ditunggu ya update berikutnya! :)")
	print("Berikut score yang berhasil kamu proleh : ", qzscore, "/ 10\n\n")
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.8 - RFUM
def rfum():
	clear()
	b4()
	try:
		print(f"Time Now	: {waktu}")
		tb = input("\nSelamat datang di program RFUM, silahkan tekan enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	except EOFError:
		print('\n[!] Error : CTRL + D Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	rekfm()
# 3.8.1 - Main RFUM
def rekfm():
	action = ['Avengers', 'Tenet', 'Transformers', 'The Expendable', 'Fast & Furious', 'Pacific Rim', 'Nobody', 'Jurrasic World', 'Justice League', 'Mortal Kombat']
	romance = ['500 Days of Summer', '10 Things I hate About You', 'Mr. and Mrs Smith', 'Paper Towns', 'The Fault in Our Stars', 'Kimi No Nawa', 'Friends With Benefits', 'Pride and Prejudice', 'Cinderlla', "Beauty and The Beast"]
	horror = ['The Medium', 'The Counjuring', 'The Insidious', 'A Quiet Place', 'Mata Batin', 'The Tall Grass', 'Bird Box', 'The Curse of La Llorona', 'Sabrina', 'Impetigore']
	comedy = ['Red Notice', 'Deadpool', 'Free Guy', 'Kungfu Hustle', 'Jumanji', 'My Stupid Bos', 'Yowis Ben', 'Reuni Z', 'The Guys', 'Susah Sinyal']
	scifi = ['Spider-Man', 'Iron-Man', 'Venom', 'Godzilla', 'Terminator', 'Evangelion', 'Prometheus', 'Alien: Covenant', 'Captain America', '2012']
	print("Silahkan pilih genre film yang kalian mau (a)ction/(r)omance/(h)orror/(c)omedy/(s)cifi/(e)xit :")
	cek_genre = input("Pilihanmu : ")
	while True:
		if cek_genre.lower() == "a":
			print("Pilihan film yang bagus untukmu adalah :")
			print("1.", action[0])
			print("2.", action[1])
			print("3.", action[2])
			print("4.", action[3])
			print("5.", action[4])
			print("6.", action[5])
			print("7.", action[6])
			print("8.", action[7])
			print("9.", action[8])
			print("10.", action[9])
			time.sleep(1)
			while True:
				response = input("Ingin kembali? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekfm()
				elif response.lower() == "n":
					clear()
					print("[!] Selamat tinggal, dadah :)")
					time.sleep(2)
					exit()
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif cek_genre.lower() == "r":
			print("Pilihan film yang bagus untukmu adalah :")
			print("1.", romance[0])
			print("2.", romance[1])
			print("3.", romance[2])
			print("4.", romance[3])
			print("5.", romance[4])
			print("6.", romance[5])
			print("7.", romance[6])
			print("8.", romance[7])
			print("9.", romance[8])
			print("10.", romance[9])
			time.sleep(1)
			while True:
				response = input("Ingin kembali ke main menu? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekfm()
				elif response.lower() == "n":
					clear()
					print("[!] Selamat tinggal, dadah :)")
					time.sleep(2)
					exit()
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif cek_genre.lower() == "h":
			print("Pilihan film yang bagus untukmu adalah :")
			print("1.", horror[0])
			print("2.", horror[1])
			print("3.", horror[2])
			print("4.", horror[3])
			print("5.", horror[4])
			print("6.", horror[5])
			print("7.", horror[6])
			print("8.", horror[7])
			print("9.", horror[8])
			print("10.", horror[9])
			time.sleep(1)
			while True:
				response = input("Ingin kembali ke main menu? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekfm()
				elif response.lower() == "n":
					clear()
					print("[!] Selamat tinggal, dadah :)")
					time.sleep(2)
					exit()
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif cek_genre.lower() == "c":
			print("Pilihan film yang bagus untukmu adalah :")
			print("1.", comedy[0])
			print("2.", comedy[1])
			print("3.", comedy[2])
			print("4.", comedy[3])
			print("5.", comedy[4])
			print("6.", comedy[5])
			print("7.", comedy[6])
			print("8.", comedy[7])
			print("9.", comedy[8])
			print("10.", comedy[9])
			time.sleep(1)
			while True:
				response = input("Ingin kembali ke main menu? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekfm()
				elif response.lower() == "n":
					clear()
					print("[!] Selamat tinggal, dadah :)")
					time.sleep(2)
					exit()
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif cek_genre.lower() == "s":
			print("Pilihan film yang bagus untukmu adalah :")
			print("1.", scifi[0])
			print("2.", scifi[1])
			print("3.", scifi[2])
			print("4.", scifi[3])
			print("5.", scifi[4])
			print("6.", scifi[5])
			print("7.", scifi[6])
			print("8.", scifi[7])
			print("9.", scifi[8])
			print("10.", scifi[9])
			time.sleep(1)
			while True:
				response = input("Ingin kembali ke main menu? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					rekfm()
				elif response.lower() == "n":
					clear()
					print("[!] Selamat tinggal, dadah :)")
					time.sleep(2)
					exit()
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif cek_genre.lower() == "e":
			time.sleep(1)
			clear()
			b1()
			menu()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.9 - Kalkulator Sederhana
def kalk():
	clear()
	b5()
	try:
		print(f"Time Now	: {waktu}")
		tb = input("\nSelamat datang di program Kalkulator Sederhana, silahkan tekan enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	except EOFError:
		print('\n[!] Error : CTRL + D Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	mkalk()
# 3.9.1 - Main Kalkulator
def mkalk():
	print("Silahkan masukan angka pertama, operator, dan angka kedua")
	time.sleep(1)
	angka_1 = float(input("masukan angka 1 = "))
	operator = input("operator (+,-,x,/) : ")
	angka_2 = float(input("masukan angka 2 = "))
	while True:
		if operator == "+": # Penjumlahan
			hasil = angka_1 + angka_2
			print(f"Hasilnya adalah {hasil:.2f}")
			while True:
				response = input("Ingin kembali menghitung? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					mkalk()
				elif response.lower() == "n":
					time.sleep(1)
					while True:
						response = input("Ingin kembali ke main menu? (y/n) ")
						if response == "y":
							time.sleep(1)
							clear()
							b1()
							menu()
						elif response == "n":
							clear()
							print("[!] Selamat tinggal, dadah :)")
							time.sleep(2)
							exit()
						else:
							print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
							time.sleep(1)
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif operator == "-": # Pengurangan
			hasil = angka_1 - angka_2
			print(f"Hasilnya adalah {hasil:.2f}")
			while True:
				response = input("Ingin kembali menghitung? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					mkalk()
				elif response.lower() == "n":
					time.sleep(1)
					while True:
						response = input("Ingin kembali ke main menu? (y/n) ")
						if response == "y":
							time.sleep(1)
							clear()
							b1()
							menu()
						elif response == "n":
							clear()
							print("[!] Selamat tinggal, dadah :)")
							time.sleep(2)
							exit()
						else:
							print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
							time.sleep(1)
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif operator == "x" or operator == "*": # Perkalian
			hasil = angka_1 * angka_2
			print(f"Hasilnya adalah {hasil:.2f}")
			while True:
				response = input("Ingin kembali menghitung? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					mkalk()
				elif response.lower() == "n":
					time.sleep(1)
					while True:
						response = input("Ingin kembali ke main menu? (y/n) ")
						if response == "y":
							time.sleep(1)
							clear()
							b1()
							menu()
						elif response == "n":
							clear()
							print("[!] Selamat tinggal, dadah :)")
							time.sleep(2)
							exit()
						else:
							print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
							time.sleep(1)
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		elif operator == "/": # Pembagian
			hasil = angka_1 / angka_2
			print(f"Hasilnya adalah {hasil:.2f}")
			while True:
				response = input("Ingin kembali menghitung? (y/n) ")
				if response.lower() == "y":
					time.sleep(1)
					clear()
					mkalk()
				elif response.lower() == "n":
					time.sleep(1)
					while True:
						response = input("Ingin kembali ke main menu? (y/n) ")
						if response == "y":
							time.sleep(1)
							clear()
							b1()
							menu()
						elif response == "n":
							clear()
							print("[!] Selamat tinggal, dadah :)")
							time.sleep(2)
							exit()
						else:
							print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
							time.sleep(1)
				else:
					print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
					time.sleep(1)
		else:
			print("Masukan angka yang bener dong ah")

# 3.10 - About me
def abt():
	clear()
	b8()
	print(f"Time Now	: {waktu}")
	print("""\nHalo... Sebelumnya perkenalkan, nama saya yn. Saya bekerja untuk PT. cinta abadi. 
Hobi saya mantengin foto doi. Keseharian BMMMT (Bangun, Makan, Mandi, Mleyot, Tidur). 
Udah punya pawang, cantik trs manis beud subhanallah masyaallah allahuakbar.
Mental sedikit keganggu, Kesehatan ya bgt, Makan masih nasi, Minum masih aqua. Stress dengan per osisan. 
Kata kata motivasi "with great power, comes great responsibility" - dari film spiderman.
Buka jasa desain logo, pamflet, banner, dll. Buka juga jasa install ulang OS. Japri aja kalo minat.
Dulu ku wibu, sekarang ku bucin. Gimana ga bucin anjir cewe gua cakep banget aaaaaaaannnnnnnnnnjiiiiiiiiir.
Twitter ada, tapi isinya keluh kesah kehidupan. Gausa dicari. Kalo FB buat repost meme, jangan dicari juga.
IG gada apa apanya, jangan difollow. Dah gt aja, kalo mau tau lebih lanjut bisa japri aja langsung ke orangnya. BYE.\n\n
		""")
	while True:
		response = input("About You? (y/n) ")
		if response.lower() == "y":
			if usr[0] == "fazila":
				time.sleep(1)
				clear()
				abty()
			else:
				print("Maaf, kamu tidak bisa mengakses menu ini\nSilahkan kembali...")
				time.sleep(1)
				clear()
				b1()
				menu()
		elif response.lower() == "n":
			time.sleep(1)
			clear()
			b1()
			menu()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.x - ?
def abty():
	print("Nama kamu", usr[0], ", kamu lahir tanggal", aby[0], ", kamu tinggal di", aby[1])
	time.sleep(3)
	print("dan sekarang kamu sekolah di", aby[2], "ambil jurusan", aby[3], ".")
	time.sleep(3)
	print("Kamu sudah punya pacar, yang bernama", aby[4], "ya kan?")
	time.sleep(2)
	print("Ya... Yang berarti kamu pacar saya, hehe...")
	print("Jiaaaakkkkhhhh")
	time.sleep(3)
	print("\nHalo cantik, gmn kabarnya sekarang? Semoga sehat sehat terus ya...")
	time.sleep(3)
	print("Itu mukanya jangan manis manis, saia takut saingan sama semut :(")
	time.sleep(3)
	print("Sip, dikit aja dulu. Semoga suka ya manisss....")
	time.sleep(3)
	print("Salam titik koma,")
	print("ur bf,")
	print("\nyn\n\n")
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

	
# 4 - Banner
# 4.1 - Start banner
def b1():
	print('                   _         _    ')
	print('                  | |       | |   ')
	print('  __ _ _ __  _ __ | | _____ | | __')
	print(' / _` | \'_ \\| \'_ \\| |/ / _ \\| |/ /')
	print('| (_| | |_) | |_) |   < (_) |   < ')
	print(' \\__, | .__/| .__/|_|\\_\\___/|_|\\_\\ ')
	print('  __/ | |   | |__________________ ')
	print(' |___/|_|   |____________________|\n')

# 4.2 - Tebak-tebakan banner
def b2():
	print(' _   _     _    _   _     _               ')
	print('| | | |   | |  | | | |   | |              ')
	print('| |_| |__ | | _| |_| |__ | | ____ _ _ __  ')
	print('| __| \'_ \\| |/ / __| \'_ \\| |/ / _` | \'_ \\ ')
	print('| |_| |_) |   <| |_| |_) |   < (_| | | | |')
	print(' \\__|_.__/|_|\\_\\\\__|_.__/|_|\\_\\__,_|_| |_|')
	print('-------------------------------------------')

# 4.3 - Quiz banner
def b3():
	print('             _     ')
	print('            (_)    ')
	print('  __ _ _   _ _ ____')
	print(' / _` | | | | |_  /')
	print('| (_| | |_| | |/ / ')
	print(' \\__, |\\__,_|_/___|')
	print('    | |            ')
	print('    |_|            ')
	print('-------------------')

# 4.4 - Rekomendasi Film Untuk Mu
def b4():
	print('        __                 ')
	print('       / _|                ')
	print('  _ __| |_ _   _ _ __ ___  ')
	print(' | \'__|  _| | | | \'_ ` _ \ ')
	print(' | |  | | | |_| | | | | | |')
	print(' |_|  |_|  \__,_|_| |_| |_|')
	print('---------------------------')

# 4.5 - Kalkulator Sederhana
def b5():
	print(' _  __     _ _          _       _             ')
	print('| |/ /    | | |        | |     | |            ')
	print('| \' / __ _| | | ___   _| | __ _| |_ ___  _ __ ')
	print('|  < / _` | | |/ / | | | |/ _` | __/ _ \| \'__|')
	print('| . \ (_| | |   <| |_| | | (_| | || (_) | |   ')
	print('|_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|   ')
	print('----------------------------------------------')

# 4.7 - About me banner
def b8():
	print('       _                 _                  ')
	print('      | |               | |                 ')
	print('  __ _| |__   ___  _   _| |_ _ __ ___   ___ ')
	print(' / _` | \'_ \\ / _ \\| | | | __| \'_ ` _ \\ / _ \\')
	print('| (_| | |_) | (_) | |_| | |_| | | | | |  __/')
	print(' \\__,_|_.__/ \\___/ \\__,_|\\__|_| |_| |_|\\___|')
	print('--------------------------------------------')


# 5 - Start
if __name__ == "__main__":
	start()