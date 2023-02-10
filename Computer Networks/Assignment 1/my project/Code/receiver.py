import helper

class Receiver:
	#Initialize all the data members of class
	def __init__(self, s):
		self.codewords = s.codewords
		self.dataSize = s.dataSize
		self.sentparity = s.parity
		self.receivedparity = ""
		self.sentchecksum = s.checksum
		self.sum = ""
		self.addchecksum = ""
		self.complement = ""
	
	#Function to decode and check for error in codewordss
	def checkError(self, type, poly=""):
		if type == 1:
			for i in range(len(self.codewords)):
				countOnes = 0
				for j in range(len(self.codewords[i])):
					if self.codewords[i][j]=='1':
						countOnes += 1
				if countOnes%2==0:
					print("Parity is even.", end=' ')
					print("NO ERROR DETECTED")
				else:
					print("Parity is odd.", end=' ')
					print("ERROR DETECTED")
		elif type == 2:
			error = False
			i=0
			while i<self.dataSize:
				countOnes = 0
				j=0
				while j<len(self.codewords):
					if self.codewords[j][i] == '1':
						countOnes += 1
					j+=1
				if countOnes%2==1:
					ch = '1'
				else:
					ch = '0'
				self.receivedparity += ch	
				if ch != self.sentparity[i]:
					error = True
				i+=1
			if error:
				print("Parity did not match.",end=' ')
				print("ERROR DETECTED")
			else:
				print("Parity matched.",end=' ')
				print("NO ERROR DETECTED")
		elif type == 3:
			self.sum = self.calculateSum()
			result = helper.add(self.sum, self.sentchecksum)
			while len(result) > self.dataSize:
				t1 = result[:len(result)-self.dataSize]
				t2 = result[len(result)-self.dataSize:]
				result = helper.add(t1, t2)
			self.addchecksum = result
			
			#finding complement and checking error
			error = False
			for ch in self.addchecksum:
				if ch == '0':
					self.complement += '1'
					error = True
				else:
					self.complement += '0'
			if error:
				print("Complement is not zero.",end=' ')
				print("ERROR DETECTED")
			else:
				print("Complement is zero.",end=' ')
				print("NO ERROR DETECTED")
		elif type == 4:
			for i in range(len(self.codewords)):
				remainder = helper.divide(self.codewords[i], poly)
				error = False
				for j in range(len(remainder)):
					if remainder[j] == '1':
						error = True
				print("Remainder:",remainder,end=' ')
				if error:
					print("ERROR DETECTED")
				else:
					print("NO ERROR DETECTED")
		print()
			
	#Function to display the received codewordss
	def displayData(self, type):
		print("codewords received by receiver:")
		print(self.codewords)
		print("\n")
		if type == 2:
			print(self.receivedparity, " - parity")
		elif type == 3:
			print(self.sum, " - sum")
			print(self.addchecksum, " - sum + checksum")
			print(self.complement, " - complement")	
		for i in range(len(self.codewords)):
			self.codewords[i] = self.codewords[i][:self.dataSize]
		print("Extracting datawords from codewordss:")
		print(self.codewords)
		print("\n")
		print()


	def calculateSum(self):
		result = self.codewords[0]
		for i in range(1,len(self.codewords)):
			result = helper.add(result, self.codewords[i])
			while len(result) > self.dataSize:
				t1 = result[:len(result)-self.dataSize]
				t2 = result[len(result)-self.dataSize:]
				result = helper.add(t1, t2)
		return result