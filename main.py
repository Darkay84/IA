#!E:/Python27/python.exe
#-*- coding: UTF-8 -*-

import morpion

while(True) :
	theMorpion = morpion.Morpion()

	while(theMorpion.run) : theMorpion.play()

raw_input()