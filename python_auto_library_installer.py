import os
paketler = ["django","kivy","facebook-sdk","google","pygame","pandas","numpy","schedule","opencv-python","scrapy","requests","wxPython","pillow","SQLAlchemy==1.3.15","beautifulsoup4","twisted","scipy","matplotlib","--upgrade --user pyglet","pywin32","nltk","nose"]

print("****************Oto Paket Yükleyiciye Hoşgeldiniz*********************")
print("****************Paketleri Otomatik Kurmak İçin 1'e Basın**************")
print("****************Paketleri El ile Kurmak İçin 2'ye Basın***************")
secim= input("")

if secim =="1":
	print("**************************************************************")
	print("*************AGARTHA CYBER WARRİOR LOJİSTİK*******************")
	print("**************************************************************")
	for i in paketler:
		os.system("pip install "+i)

		
		print("*************************************")
		print("*************************************")
		print("********** "+ i +" Yüklendi**********") 
		print("*************************************")
		print("*************************************")
	
if secim == "2":
	while True:
		paket = input("Paket Adını Yazınız  ")
		os.system("pip install "+paket)
		print("ÇIKMAK İÇİN CTRL VE C TUŞLARINA AYNI ANDA BASIN")

print("********************İşlem Tamamlandı**************************")
print("*************AGARTHA CYBER WARRİOR LOJİSTİK*******************")
print("**************************************************************")
