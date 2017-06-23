# -*- coding: utf-8 -*-
__author__ = 'mocobk'


import msvcrt
import sys


while True:
	# key = str(msvcrt.getch()).split("'")[1]
	
	# print("你输入的是%s" %key)
	key2 = msvcrt.getch()
	# print(key2)
	if ord(key2) == 3:
		exit(0)
	print("ascall码是:%s" %ord(key2))
	print("键      是:%s" %key2)
	
