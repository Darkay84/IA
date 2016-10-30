#!E:/Python27/python.exe
#-*- coding: UTF-8 -*-

class Morpion :

	import random
	import os

	def __init__(self) :
		self.table = {}
		self.table[0,0] = ' '
		self.table[0,1] = ' '
		self.table[0,2] = ' '
		self.table[1,0] = ' '
		self.table[1,1] = ' '
		self.table[1,2] = ' '
		self.table[2,0] = ' '
		self.table[2,1] = ' '
		self.table[2,2] = ' '

		self.player = True

		self.run = True

		self.counter = 0

	def clear(self) :
		self.os.system("cls")

	def printLine(self, i) :
		print "|", str(self.table[i, 0]), "|", str(self.table[i, 1]), "|", str(self.table[i, 2]), "|"
		return ""

	def printTable(self) :
		print "-------------"
		print "|", str(self.table[0, 0]), "|", str(self.table[0, 1]), "|", str(self.table[0, 2]), "|"
		print "-------------"
		print "|", str(self.table[1, 0]), "|", str(self.table[1, 1]), "|", str(self.table[1, 2]), "|"
		print "-------------"
		print "|", str(self.table[2, 0]), "|", str(self.table[2, 1]), "|", str(self.table[2, 2]), "|"
		print "-------------"
		return ""

	def twoInARaw(self, char) :
		count = 0
		for i in range(3) :
			if self.table[i, 0] == char and self.table[i, 1] == char :
				count = count + 1
			elif self.table[i, 1] == char and self.table[i, 2] == char :
				count = count + 1
			elif self.table[i, 0] == char and self.table[i, 2] == char :
				count = count + 1

			if self.table[0, i] == char and self.table[1, i] == char :
				count = count + 1
			elif self.table[1, i] == char and self.table[2, i] == char :
				count = count + 1
			elif self.table[0, i] == char and self.table[2, i] == char :
				count = count + 1

		if self.table[0, 0] == char and self.table[1, 1] == char :
			count = count + 1
		elif self.table[1, 1] == char and self.table[2, 2] == char :
			count = count + 1
		elif self.table[0, 0] == char and self.table[2, 2] == char :
			count = count + 1

		if self.table[0, 2] == char and self.table[1, 1] == char :
			count = count + 1
		elif self.table[1, 1] == char and self.table[2, 0] == char :
			count = count + 1
		elif self.table[0, 2] == char and self.table[2, 0] == char :
			count = count + 1

		return count

	def threeInARow(self, char) :
		for i in range(3) :
			if self.table[i, 0] == char and self.table[i, 1] == char and self.table[i, 2] == char :
				return 1
			if self.table[0, i] == char and self.table[1, i] == char and self.table[2, i] == char :
				return 1

		if self.table[0, 0] == char and self.table[1, 1] == char and self.table[2, 2] == char :
			return 1

		if self.table[0, 2] == char and self.table[1, 1] == char and self.table[2, 0] == char :
			return 1

		return 0

	def play(self) :
		if self.player :
			print "\n----PLAYER > ROUND " + str(self.counter)  + "----\n"

			x = input("Enter a value x : ")

			while x < 1 or x > 3 :
				x = input("Value must be between 1 and 3 inclusive !")

			y = input("Enter a value y : ")

			while y < 1 or y > 3 :
				y = input("Value must be between 1 and 3 inclusive !")

			while self.table[y - 1, x - 1] != ' ' :
				print "This position is already in use :/"

				x = input("Enter a value x : ")

				while x < 1 or x > 3 :
					x = input("Value must be between 1 and 3 inclusive !")

				y = input("Enter a value y : ")

				while y < 1 or y > 3 :
					y = input("Value must be between 1 and 3 inclusive !")

			self.counter += 1
			self.table[y - 1, x - 1] = 'X'
		else :
			print "\n---COMPUTER > ROUND " + str(self.counter)  + "---\n"

			self.counter += 1
			self.playIA(2)

		self.player = not self.player

		#self.clear()

		self.printTable()

		if self.threeInARow('X') : 
			print "-------------"
			print "Player won !"
			self.run = False
			raw_input()
			self.clear()

		elif self.threeInARow('O') :
			print "-------------"
			print "Computer won !"
			self.run = False
			raw_input()
			self.clear()

		elif self.counter >= 9 :
			print "-------------"
			print "No winner :/"
			self.run = False
			raw_input()
			self.clear()

	def playIA(self, deepness, computer = True) :
		maxValue = -5000
		bestx, besty = 0, 0

		for j in range(3) :
			for i in range(3) :
				if self.table[i, j] == ' ' :
					if computer :
						self.table[i, j] = 'O'
					else :
						self.table[i, j] = 'X'
					value = self.theMin(deepness, not computer)

					if value > maxValue :
						maxValue = value
						bestx = i
						besty = j

					self.table[i, j] = ' '

		if self.twoInARaw('X') == 0 :
			bestx, besty = self.random.randint(0, 2), self.random.randint(0, 2)

		while self.table[bestx, besty] != ' ' :
			bestx, besty = self.random.randint(0, 2), self.random.randint(0, 2)
			
		self.table[bestx, besty] = 'O'

	def theMin(self, deepness, computer) :
		if deepness == 0 or self.threeInARow('X') or self.threeInARow('O') :
			return self.evaluate()

		minValue = 5000

		for j in range(3) :
			for i in range(3) :
				if self.table[i, j] == ' ' :
					if computer :
						self.table[i, j] = 'O'
					else :
						self.table[i, j] = 'X'
					value = self.theMax(deepness - 1, not computer)

					if value < minValue :
						minValue = value

					self.table[i, j] = ' '

		return minValue

	def theMax(self, deepness, computer) :
		if deepness == 0 or self.threeInARow('X') or self.threeInARow('O') :
			return self.evaluate()

		maxValue = -5000

		for j in range(3) :
			for i in range(3) :
				if self.table[i, j] == ' ' :
					if computer :
						self.table[i, j] = 'O'
					else :
						self.table[i, j] = 'X'
					value = self.theMin(deepness - 1, not computer)

					if value > maxValue :
						maxValue = value

					self.table[i, j] = ' '

		return maxValue

	def evaluate(self) :
		if self.threeInARow('X') or self.threeInARow('O') :
			if self.threeInARow('X') :
				return -1000 + self.counter
			elif self.threeInARow('O') :
				return 1000 - self.counter
			else :
				return 0

		return self.twoInARaw('O') - self.twoInARaw('X')