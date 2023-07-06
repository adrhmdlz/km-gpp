# def user():
# 	name = str(input("How do i call you? : "))
# 	try:
# 		if name.lower() == "fazila":
# 			usr.append(name)
# 			bd = "22 Agustus 2004"
# 			aby.append(bd)
# 			tl = "Malang"
# 			aby.append(tl)
# 			ns = "SMK Telkom Malang"
# 			aby.append(ns)
# 			nj = "RPL"
# 			aby.append(nj)
# 			np = "adrian"
# 			aby.append(np)
# 			time.sleep(2)
# 			loading()
# 		elif name.lower() == "":
# 			alt_name = "Catfish"
# 			response = input(f"Kalo aku panggil kamu {alt_name}, boleh ga? (y/n/terserah) ")
# 			if response.lower() == "y":
# 				name = alt_name
# 				usr.append(name)
# 				print(f"Asikk, mulai sekarang aku panggil kamu {name}")
# 				time.sleep(2)
# 				loading()
# 			elif response.lower() == "n":
# 				print(f"Ah kamu ga asik!")
# 				time.sleep(2)
# 				clear()
# 				user()
# 			elif response.lower() == "terserah":
# 				print(f"Yaudah kamu aku panggil {alt_name} aja")
# 				name = alt_name
# 				usr.append(name)
# 				time.sleep(2)
# 				loading()
# 			elif response.lower() == "":
# 				print("Ah kamu ga asik :(")
# 				time.sleep(2)
# 				clear()
# 				user()
# 			else:
# 				response = input(f"Yang bener!! (y/n/terserah) ")
# 				if response == "y":
# 					name = alt_name
# 					usr.append(name)
# 					print(f"OKE")
# 					time.sleep(2)
# 					loading()
# 				elif response == "n":
# 					print("Yaudah bye bye!")
# 					time.sleep(2)
# 					quit()
# 				elif response == "terserah":
# 					print(f"Yaudah kamu aku panggil {alt_name} aja")
# 					name = alt_name
# 					usr.append(name)
# 					time.sleep(2)
# 					loading()
# 		else:
# 			usr.append(name)
# 			time.sleep(2)
# 			loading()
# 	except KeyboardInterrupt:
# 		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
# 		time.sleep(2)
# 		quit()
# 	clear()
# 	user()