#!/bin/python
# coding: utf-8
#####by kevo (g1ng3rb1t3) ;)
try:
	import time
	import os
	import sys
	import requests
	from sys import exit
	from time import sleep
	import colorama
	from colorama import Fore, Back, Style
	from tqdm import tqdm
	import time
	import pyshorteners
	from time import *
	from platform import python_version
	os.system('clear')
	On_Red = '\033[41m'
	now = strftime("%T")
	colorama.init(autoreset = True)
	green = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
	carol = Style.RESET_ALL
	white = Style.DIM+Fore.WHITE
	magenta = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
	yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
	red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
	blue = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
	os.system('toilet --gay -f emboss -F border " Welcome To Cvirus"')
	def MainHome():
		print('+'*19,'[',now,']','+'*19)
		print('{}[{}01{}] {}Android\t\t\t{}[{}06{}] {}Worm and Bomb'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}02{}] {}Shell virus\t\t{}[{}07{}] {}About'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}03{}] {}Pdf\t\t\t{}[{}08{}] {}Surprise'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}04{}] {}Windows\t\t\t{}[{}09{}] {}Update'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}05{}] {}MacOsX\t\t\t{}[{}10{}] {}Exit'.format(blue,red,blue,yellow,blue,red,blue,On_Red))
		menuopt = input('{}>>>>> {}'.format(white,green))
		if menuopt in ('1','01'):
			sleep(2)
			Android()
		elif menuopt in ('2','02'):
			sleep(2)
			ShellVirus()
		elif menuopt in ('3','03'):
			sleep(2)
			PdfVirus()
		elif menuopt in ('4','04'):
			sleep(2)
			WindowsVirus()
		elif menuopt in ('5','05'):
			sleep(2)
			MacOsx()
		elif menuopt in ('6','06'):
			sleep(2)
			WormAndBomb()
		elif menuopt in ('7','07'):
			sleep(2)
			About()
		elif menuopt in ('8','08'):
			Surprise()
		elif menuopt in ('9','09'):
			print('') #update
		elif menuopt == '10':
			sleep(5)
			sys.exit('Closing......')
		else :
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def Android():
		print('{}[{}01{}] {}Agent\t\t{}[{}21{}] {}Cat'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}02{}] {}Badnews\t\t{}[{}22{}] {}ChistesCortos'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}03{}] {}Bios\t\t{}[{}23{}] {}Chistepicanticos'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}04{}] {}BlatanSMS\t\t{}[{}24{}] {}FunnyYs'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}05{}] {}BrainTest\t\t{}[{}25{}] {}Image Pets'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}06{}] {}Claco\t\t{}[{}26{}] {}Kitchen'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}07{}] {}DropDialer\t\t{}[{}27{}] {}Laughter'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}08{}] {}FakeBank\t\t{}[{}28{}] {}Prasesamor'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}09{}] {}FakeCMCC\t\t{}[{}29{}] {}PrasesFee'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}10{}] {}FakeDoc\t\t{}[{}30{}] {}RecipeSmart'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}11{}] {}FakeValidation\t{}[{}31{}] {}RomaticPoss'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}12{}] {}Fobus\t\t{}[{}32{}] {}StateSSS'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}13{}] {}GinMaster\t\t{}[{}33{}] {}ThinKing'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}14{}] {}Masnu\t\t{}[{}34{}] {}Crd'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}15{}] {}Elite\t\t{}[{}35{}] {}Dendroid'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}16{}] {}Omigo\t\t{}[{}36{}] {}Ds'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}17{}] {}OpFake\t\t{}[{}37{}] {}Facebook'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}18{}] {}Sms Worker\t\t{}[{}38{}] {}Fake_Av'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}19{}] {}Vietcon\t\t{}[{}39{}] {}ADware'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}20{}] {}Candy Corn\t\t{}[{}40{}] {}Mp3Player'.format(blue,red,blue,yellow,blue,red,blue,yellow))
		print('{}[{}Enter{}] {}Press 2 times\t{}[{}41{}] {}Settings'.format(blue,On_Red,blue,yellow,blue,red,blue,yellow))
		androvi = input('{}>>>>> {}'.format(white,green))
		if androvi in ('1','01'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Agent.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Agent.apk?raw=true' Android/Agent.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('2','02'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BadNews.A.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'BadNews.A.apk?raw=true' Android/BadNews.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('03','3'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Bios.NativeMaliciousCode.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Bios.NativeMaliciousCode.apk?raw=true' Android/Bios.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('4','04'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Blatantsms.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Blatantsms.apk?raw=true' Android/Blatantsms.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('5','05'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/BrainTest.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'BrainTest.apk?raw=true' Android/BrainTest.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('6','06'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Claco.A.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Claco.A.apk?raw=true' Android/Claco.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('7','07'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Dropdialer.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Dropdialer.apk?raw=true' Android/DropDialer.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('8','08'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeBank.B.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'FakeBank.B.apk?raw=true' Android/FakeBank.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi in ('9','09'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeCMCC.A.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'FakeCMCC.A.apk?raw=true' Android/FakeCMCC.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '10':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeDoc.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'FakeDoc.apk?raw=true' Android/FakeDoc.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '11':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/FakeValidation.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'FakeValidation.apk?raw=true' Android/FakeValidation.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '12':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fobus.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Fobus.apk?raw=true' Android/Fobus.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '13':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/GinMaster.Z.AdvancedObfuscation.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'GinMaster.Z.AdvancedObfuscation.apk?raw=true' Android/GinMaster.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '14':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Masnu.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Masnu.apk?raw=true' Android/Masnu.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '15':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Minecraft2.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Minecraft2.apk?raw=true' Android/Elite.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '16':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Omigo.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Omigo.apk?raw=true' Android/Omigo.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '17':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Opfake.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Opfake.apk?raw=true' Android/Opfake.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '18':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/SmsWorker.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'SmsWorker.apk?raw=true' Android/SmsWorker.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '19':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Vietcon.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Vietcon.apk?raw=true' Android/Vietcon.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '20':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/candy_corn.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'candy_corn.apk?raw=true' Android/Candycorn.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '21':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/cat.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'cat.apk?raw=true' Android/Cat.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '22':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/chistescortos.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'chistescortos.apk?raw=true' Android/Chistescortos.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '23':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/chistespicanticos.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'chistespicanticos.apk?raw=true' Android/Chistespicanticos.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '24':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.funnyys.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.funnyys.apk?raw=true' Android/ComFunnys.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '25':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.imagepets.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.imagepets.apk?raw=true' Android/ComImagePets.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '26':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.kitchenn.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.kitchenn.apk?raw=true' Android/ComKitchen.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '27':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.laughtter.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.laughtter.apk?raw=true' Android/ComLaughtter.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '28':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesamor.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.prasesamor.apk?raw=true' Android/Prasesamor.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '29':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.prasesfee.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.prasesfee.apk?raw=true' Android/Prasesfee.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '30':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.recipesmart.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.recipesmart.apk?raw=true' Android/Recipesmart.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '31':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.romaticpos.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.romaticpos.apk?raw=true' Android/Romaticpos.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '32':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.statetss.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.statetss.apk?raw=true' Android/Statetss.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '33':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/com.thinkking.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'com.thinkking.apk?raw=true' Android/Thinkking.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '34':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/crd.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'crd.apk?raw=true' Android/Crd.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '35':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/dendroid.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'dendroid.apk?raw=true' Android/Dendroid.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '36':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ds.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'ds.apk?raw=true' Android/Ds.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '37':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/facebook.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'facebook.apk?raw=true' Android/Facebook.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '38':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Fake_av.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Fake_av.apk?raw=true' Android/Fakeav.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '39':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ArtStation.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'ArtStation.apk?raw=true' Android/ArtStation.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '40':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Adware.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Adware.apk?raw=true' Android/MusicPlayerAdware.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == '41':
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/Settings.apk?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'Settings.apk?raw=true' Android/Settings.apk")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif androvi == input():
			print('{}[{}={}] {}Directing to main menu'.format(blue,On_Red,blue,On_Red))
			sleep(3)
			MainHome()
		else:
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def ShellVirus():
		print('{}[{}1{}] {}DataEater.sh'.format(blue,red,blue,yellow))
		print('{}[{}2{}] {}Bootloop.sh'.format(blue,red,blue,yellow))
		print('{}[{}={}] {}Press enter twice to go back'.format(blue,On_Red,blue,On_Red))
		shells = input('{}>>>>> {}'.format(white,green))
		if shells in ('1','01'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/data-eater.sh?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'data-eater.sh?raw=true' Shell-virus/Data-Eater.sh")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif shells in ('2','02'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/bootloop.sh?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'bootloop.sh?raw=true' Shell-virus/Bootloop.sh")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif shells == input():
			print('{}[{}={}] {}Directing to main menu'.format(blue,On_Red,blue,On_Red))
			sleep(3)
			MainHome()
		else:
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def PdfVirus():
		print('{}[{}01{}] {}Hack Facebook'.format(blue,red,blue,yellow))
		print('{}[{}02{}] {}How to hack facebook'.format(blue,red,blue,yellow))
		print('{}[{}={}] {}Press enter twice to go back'.format(blue,On_Red,blue,On_Red))
		pdfinput = input('{}>>>>> {}'.format(white,green))
		if pdfinput in ('01','1'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/hackfacebook.rar?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'hackfacebook.rar?raw=true' Pdf-autorun-windows/Hack-facebook.rar")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
				print("[=] password> cracker\n")
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif pdfinput in ('2','02'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/howtohackfb.rar?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'howtohackfb.rar?raw=true' Pdf-autorun-windows/How-to-hack-facebook.rar")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
				print("[=] password> cracker\n")
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif pdfinput == input():
			print('{}[{}={}] {}Directing to main menu'.format(blue,On_Red,blue,On_Red))
			sleep(3)
			MainHome()
		else:
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def WindowsVirus():
		print('{}[{}01{}] {}Ugly.bat'.format(blue,red,blue,yellow))
		print('{}[{}02{}] {}Sleep.bat'.format(blue,red,blue,yellow))
		print('{}[{}03{}] {}Reg_eater.bat'.format(blue,red,blue,yellow))
		print('{}[{}04{}] {}Kuis.bat'.format(blue,red,blue,yellow))
		print('{}[{}={}] {}Press enter twice to go back'.format(blue,On_Red,blue,On_Red))
		wininput = input('{}>>>>> {}'.format(white,green))
		if wininput in ('1','01'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ugly.bat?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'ugly.bat?raw=true' Windows/Ugly.bat")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif wininput in ('2','02'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/sleepy.bat?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'sleepy.bat?raw=true' Windows/Sleepy.bat")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif wininput in ('3','03'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/reg-eater.bat?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'reg-eater.bat?raw=true' Windows/Reg-eater.bat")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif wininput in ('4','04'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/kuis.bat?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'kuis.bat?raw=true' Windows/Kuis.bat")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif wininput == input():
			print('{}[{}={}] {}Directing to main menu'.format(blue,On_Red,blue,On_Red))
			sleep(3)
			MainHome()
		else:
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def MacOsx():
		print('{}[{}01{}] {}Nothing'.format(blue,red,blue,yellow))
		print('{}[{}02{}] {}Trinoids'.format(blue,red,blue,yellow))
		print('{}[{}={}] {}Press enter twice to go back'.format(blue,On_Red,blue,On_Red))
		macinput = input('{}>>>>> {}'.format(white,green))
		if macinput in ('1','01'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/nothing.app?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'nothing.app?raw=true' Macosx/Nothing.app")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif macinput in ('2','02'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/trinoids.app?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'trinoids.app?raw=true' Macosx/Trinoids.app")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif macinput == input():
			print('{}[{}={}] {}Directing to main menu'.format(blue,On_Red,blue,On_Red))
			sleep(3)
			MainHome()
		else:
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def WormAndBomb():
		print('{}[{}01{}] {}Worm.bat'.format(blue,red,blue,yellow))
		print('{}[{}02{}] {}Bomb.zip'.format(blue,red,blue,yellow))
		print('{}[{}={}] {}Press enter twice to go back'.format(blue,On_Red,blue,On_Red))
		worminput = input('{}>>>>> {}'.format(white,green))
		if worminput in ('1','01'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/worm.bat?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'worm.bat?raw=true' Worm-and-Bombzip/worm.bat")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif worminput in ('02','2'):
			try:
				chunk_size = 1024
				url = 'https://github.com/Ractomes/Viruses/blob/master/samples/bom-zip.zip?raw=true'
				r = requests.get(url, stream = True)
				size = int(r.headers['content-length'])
				filename = url.split('/')[-1]
				with open(filename, 'wb') as f:
					for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
						f.write(data)
				os.system("mv 'bom-zip.zip?raw=true' Worm-and-Bombzip/Bomb.zip")
				print('{}[{}✓{}] {}Download success'.format(blue,yellow,blue,green))
			except:
				print('{}[{}!{}] {}Error Downloading'.format(blue,On_Red,blue,On_Red))
				sleep(3)
				print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
				sleep(5)
		elif worminput == input():
			print('{}[{}={}] {}Directing to main menu'.format(blue,On_Red,blue,On_Red))
			sleep(3)
			MainHome()
		else:
			print('{}[{}!{}] {}ERRor input'.format(blue,On_Red,blue,On_Red))
			sleep(2)
			print('{}[{}{}{}] {}Retry'.format(blue,On_Red,now,blue,On_Red))
			sleep(2)
			sys.exit('{}[{}X{}] {}Closed'.format(blue,On_Red,blue,On_Red))
	def About():
		abo = "This script is made by kelvin (g1ng3rb1t3)\nwith reference from Malicious tool @copyright\nIf you come across any errors please let me know\nRegards\ntelegram = https://t.me/iamk3lv1n\n\n\n"
		print(abo)
	def Surprise():
		print('{}[=] {}Python link shortener'.format(blue,green))
		a = input ('{}[=] {}Input url to shorten> {}'.format(blue,white,green))
		s = pyshorteners.Shortener()
		try:
			print(s.tinyurl.short(a))
		except:
			print('{}[{}X{}] {} an ERRor occured'.format(blue,On_Red,blue,On_Red))
	MainHome() #checkinternet()
except KeyboardInterrupt:
	print('{}[{}!{}] {}Cancelled'.format(blue,On_Red,blue,On_Red))
	print('{}[{}+{}] {}Created by {}g1ng3rb1t3'.format(blue,green,blue,yellow,On_Red))
	print('{}[{}={}] {}https://t.me/Iamk3lv1n'.format(blue,red,blue,green))
	
