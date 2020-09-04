#!/bin/python
# coding: utf-8
#####by kevo (g1ng3rb1t3) ;)
try:
	import os
	import sys
	from time import sleep
	from platform import python_version
	#colors
	R='\033[0;31m' #red
	G='\033[0;32m' #green
	Y='\033[0;33m' #yellow
	Z='\033[0m' #reset color
	B='\033[0;34m' #blue
	#color end
	os.system('clear')
	print('{}xxxxxxxxxxx--{}Only run this script once{}--xxxxxxxxxxx{}'.format(Y,R,Y,Z))
	sleep(6)
	print('{}----Please wait while i scan for requirements----{}'.format(G,Z))
	sleep(10)
	if int(python_version()[0]) < 3:
		print('{}[{}!{}] {}Please use Python 3 to continue'.format(B,R,B,R))
		exit()
	else:
		print('{}[=] {}Python version up to date'.format(B,G))
		sleep(2)
		def pipupdate():
			war = input('{}[=] {}Update my pip version?(y/n)'.format(B,G))
			if war in ('y','Y'):
				sleep(2)
				try:
					os.system('pip install --upgrade pip')
				except NewConnectionError:
					print('Warning')
				print('{}[=] {}updating pip'.format(B,Y))
				sleep(2)
				print('{}[×] {}updated'.format(B,G))
				sleep(2)
			elif war in ('n','N'):
				print('{}[=] {}ok moving on'.format(B,G))
				sleep(2)
			else:
				print('{}[{}X{}] {}Invalid choice!!'.format(B,R,B,R))
				sleep(1)
				pipupdate()
		pipupdate()
	try:
		import tqdm
		print('{}[×] {}Found module {}"tqdm"'.format(B,Y,G))
		sleep(2)
	except ModuleNotFoundError:
		while True:
			print('{}[X] {}You are missing module {}"tqdm"'.format(B,R,G))
			print('{}[X] {}Press enter to install it'.format(B,G))
			input()
			os.system('pip3 install tqdm')
			break
	try:
		import requests
		print('{}[×] {}Found module {}"requests"'.format(B,Y,G))
		sleep(2)
	except ModuleNotFoundError:
		while True:
			print('{}[X] {}You are missing module {}"requests"'.format(B,R,G))
			print('{}[_] {}Press enter to install it'.format(B,G))
			input()
			os.system('pip3 install requests')
			break
	try:
		import colorama
		print('{}[×] {}Found module {}"colorama"'.format(B,Y,G))
		sleep(2)
	except ModuleNotFoundError:
		while True:
			print('{}[X] {}You are missing module {}"colorama"'.format(B,R,G))
			print('{}[_] {}Press enter to install it'.format(B,G))
			input()
			os.system('pip3 install colorama')
			break
	try:
		import pyshorteners
		print('{}[×] {}Found module {}"pyshorteners"'.format(B,Y,G))
		sleep(2)
	except ModuleNotFoundError:
		while True:
			print('{}[X] {}You are missing module {}"pyshorteners"'.format(B,R,G))
			print('{}[_] {}Press enter to install it'.format(B,G))
			input()
			os.system('pip3 install pyshorteners')
			break
	try:
		print('{}---press enter to create all folders required---'.format(G))
		print('{}[{}warning{}] {}no directories then you get errors'.format(B,R,B,R))
		while True:
			input()
			#----------------------------------#
			print('{}[=] {}Creating folder for Android'.format(B,Y))
			os.system('mkdir Android')
			sleep(2)
			print('{}[=] {}Created successfully\n\n'.format(B,G))
			sleep(3)
			#-------------------------------------#
			print('{}[=] {}Creating folder for shell-virus'.format(B,Y))
			os.system('mkdir Shell-virus')
			sleep(2)
			print('{}[=] {}Created Successfully\n\n'.format(B,G))
			sleep(3)
			#-----------------------------------#
			print('{}[=] {}Creating folder for PDF'.format(B,Y))
			os.system('mkdir Pdf-autorun-windows')
			sleep(2)
			print('{}[=] {}Created Successfully\n\n'.format(B,G))
			sleep(3)
			#-----------------------------------#
			print('{}[=] {}Creating folder for Windows'.format(B,Y))
			os.system('mkdir Windows')
			sleep(2)
			print('{}[=] {}Created successfully\n\n'.format(B,G))
			sleep(3)
			#-----------------------------------#
			print('{}[=] {}Creating folder for Macosx'.format(B,Y))
			os.system('mkdir Macosx')
			sleep(2)
			print('{}[=] {}Created successfully\n\n'.format(B,G))
			sleep(3)
			#------------------------------------#
			print('{}[=] {}Creating folder for Worm-and-Bombzip'.format(B,Y))
			os.system('mkdir Worm-and-Bombzip')
			sleep(2)
			print('{}[=] {}Created successfully\n\n'.format(B,G))
			sleep(2)
			print('Created by g1ng3rb1t3')
			sleep(1)
			break
	except KeyboardInterrupt:
		print('{}[=] {}Consider creating folders'.format(B,R))
except KeyboardInterrupt:
	print('\n')
	print('{}[=] {}Closed'.format(B,R))
	print('{}[=] {}by {}g1ng3rb1t3'.format(B,Y,R))
	sys.exit()
