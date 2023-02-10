import random
import sys
from helper import *
from sender import *
from receiver import *
from medium import *

#function to generate random sequence of 0,1 and store it in a file
def generateRandomInput(length, filename):
	fileout = open(filename, "w")
	for i in range(length):
		fileout.write(str(random.randint(0,1)))
	fileout.close()

def case1(size, filename):
	puterror = True
	print("Error is detected by all four schemes.")
	print("_______________Vertical Redundancy Check___________________")
	type = 1
	s = Sender(size)
	s.createData(filename,type)
	s.displayData(type)
	if puterror:
		s.codewords = injectRandomError(s.codewords)
	r = Receiver(s)
	r.checkError(type)
	r.displayData(type)
	print("_______________Longitudinal Redundancy Check _______________-")
	type = 2
	s = Sender(size)
	s.createData(filename,type)
	s.displayData(type)
	if puterror:
		s.codewords = injectRandomError(s.codewords)
	r = Receiver(s)
	r.checkError(type)
	r.displayData(type)
	print("__________________Checksum_______________________")
	type = 3
	s = Sender(size)
	s.createData(filename,type)
	s.displayData(type)
	if puterror:
		s.codewords = injectRandomError(s.codewords)
	r = Receiver(s)
	r.checkError(type)
	r.displayData(type)
	print("_________________Cyclic Redundancy Check_________________")
	type = 4
	#poly = "1001"
	#print("Generator polynomial:",poly)
	poly = input("Enter Generator Polynomial: ")
	s = Sender(size)
	s.createData(filename,type,poly)
	s.displayData(type)
	if puterror:
		s.codewords = injectRandomError(s.codewords)
	r = Receiver(s)
	r.checkError(type,poly)
	r.displayData(type)
	
def case2(size, filename):
	print("--------------------------- CASE 2 -------------------------")
	print("Error is detected by checksum but not by CRC.")
	print("-------------- Checksum ------------------------------------")
	type = 3
	s = Sender(size)
	s.createData(filename,type)
	s.displayData(type)
	zeropos = []
	onepos = [[5]]
	s.codewords = injectAtPosError(s.codewords,zeropos,onepos)
	r = Receiver(s)
	r.checkError(type)
	r.displayData(type)
	print("-------------- Cyclic Redundancy Check ---------------------")
	type = 4
	poly = "1000"
	print("Generator Polynomial:",poly)
	s = Sender(size)
	s.createData(filename,type,poly)
	s.displayData(type)
	s.codewords = injectAtPosError(s.codewords,zeropos,onepos)
	r = Receiver(s)
	r.checkError(type,poly)
	r.displayData(type)
	print("------------------------------------------------------------\n")

#function to execute Case 3
def case3(size, filename):
	print("--------------------------- CASE 3 -------------------------")
	print("Error is detected by VRC but not by CRC.")
	print("-------------- Vertical Redundancy Check -------------------")
	type = 1
	s = Sender(size)
	s.createData(filename,type)
	s.displayData(type)
	zeropos = []
	onepos = [[5]]
	s.codewords = injectAtPosError(s.codewords,zeropos,onepos)
	r = Receiver(s)
	r.checkError(type)
	r.displayData(type)
	print("-------------- Cyclic Redundancy Check ---------------------")
	type = 4
	poly = "1010"
	print("Generator Polynomial:",poly)
	s = Sender(size)
	s.createData(filename,type,poly)
	s.displayData(type)
	s.codewords = injectAtPosError(s.codewords,zeropos,onepos)
	r = Receiver(s)
	r.checkError(type,poly)
	r.displayData(type)
	print("------------------------------------------------------------\n")

#insert case 2 and case 3
#driver function to run the error detection module
if __name__ == "__main__":
	print("------------------------------------------------------------")

	case = int(input("Enter Case Number : "))
	if case == 1:
		size = int(input("Enter length of the dataword: "))
		generateRandomInput(size*4, sys.argv[1])
		case1(size, sys.argv[1])
	elif case == 2:
		size = 8
		case2(size, sys.argv[1])
	elif case == 3:
		size = 6
		case3(size, sys.argv[1])
	else:
		print("You entered invalid choice.")   