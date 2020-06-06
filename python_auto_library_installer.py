import os
paketler = ["django","kivy","facebook-sdk","google","pygame","pandas","numpy","schedule","opencv-python","scrapy","requests","wxPython","pillow","SQLAlchemy==1.3.15","beautifulsoup4","twisted","scipy","matplotlib","pywin32","nltk","nose"]

print("****************Welcome to Auto Package Installer*********************")
print("****************Press 1 to Install Packages Automatically**************")
print("****************Press 2 to Install Packages Manually*******************")
secim= input("")

if secim =="1":
	print("**************************************************************")
	print("*************INSTAGRAM.COM/NICKZSCHE*******************")
	print("**************************************************************")
	for i in paketler:
		os.system("pip install "+i)

		
		print("*************************************")
		print("*************************************")
		print("********** "+ i +" Installed**********") 
		print("*************************************")
		print("*************************************")
	
if secim == "2":
	while True:
		paket = input("Write Package Name  ")
		os.system("pip install "+paket)
		print("Press CTRL and C at the same time to exit")

print("********************Completed**************************")
print("*************INSTAGRAM.COM/NICKZSCHE**************************")
print("************************ŞAHAN HASRET**************************")
