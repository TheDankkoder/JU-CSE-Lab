from unittest import result
from numpy import result_type
import helper

class Sender:
    #Initialize all the data members of class
    def __init__(self, size):
        self.codewords = []
        self.dataSize = size
        self.parity = ""
        self.checksum = ""
    
    #Function to generate codewordss to be sent
    def createData(self, filename, type, poly=""):
        fileinput = open(filename, "r")
        packet = fileinput.readline()
        fileinput.close()
    
#VRC
        if type == 1:
            self.VRC(packet)
#LRC
        elif type == 2:
            self.LRC(packet)
#checksum
            
        elif type == 3:
            self.checkSum(packet)     

#CRC        
        elif type == 4:
            self.CRC(packet,poly)

    #Function to display the sent codewordss
    def displayData(self, type):
        datawords = []
        for x in self.codewords:
            datawords.append(x[:self.dataSize])
        print("Datawords to be sent:")
        print(datawords)
        print("\n")
        print("codewordss sent by sender:")
        print(self.codewords)
        print("\n")
        if type == 2:
            print(self.parity, " - parity")
        elif type == 3:
            print(self.checksum, " - checksum")
        print("\n")
    
    #Helper function for VRC Even Parity generator
    def rowEvenParityGenerator(self):
        for i in range(len(self.codewords)):
            countOnes = 0
            for j in range(len(self.codewords[i])):
                if self.codewords[i][j] == '1':
                    countOnes += 1
            if countOnes%2==1:
                self.codewords[i] += '1'
            else:
                self.codewords[i] += '0'
    
    #Helper function for LRC Even Parity generator
    def columnEvenParityGenerator(self):
        i=0
        while i<self.dataSize:
            countOnes = 0
            j=0
            while j<len(self.codewords):
                if self.codewords[j][i] == '1':
                    countOnes += 1
                j+=1
            if countOnes%2==1:
                self.parity += '1'
            else:
                self.parity += '0'
            i+=1
    def calcheckSum(self):
        result = self.codewords[0]
        csum = ""
        
        for i in range(1,len(self.codewords)):
            result = helper.add(result, self.codewords[i])
            while len(result) > self.dataSize:
                t1 = result[:len(result)-self.dataSize]
                t2 = result[len(result)-self.dataSize:]
                result = helper.add(t1, t2)
        for i in range(len(result)):
                if result[i]=='0':
                    csum += '1'
                else:
                    csum += '0'
        return csum
    
    def VRC(self,packet):
        tempword=""
        for i in range(len(packet)):
                if i>0 and i%self.dataSize==0:
                    self.codewords.append(tempword)
                    tempword = ""
                tempword += packet[i]
        self.codewords.append(tempword)	
        self.rowEvenParityGenerator()

    def LRC(self,packet):
        tempword=""
        for i in range(len(packet)):
                if i>0 and i%self.dataSize==0:
                    self.codewords.append(tempword)
                    tempword = ""
                tempword += packet[i]
        self.codewords.append(tempword)	
        self.columnEvenParityGenerator()

    def checkSum(self,packet):
        tempword=""
        for i in range(len(packet)):
                if i>0 and i%self.dataSize==0:
                    self.codewords.append(tempword)
                    tempword = ""
                tempword += packet[i]
        self.codewords.append(tempword)
        self.checksum = self.calcheckSum()

    def CRC(self,packet,poly):
        tempword=""
        tempsize = self.dataSize #- (len(poly)-1)
        for i in range(len(packet)):
                if i>0 and i%tempsize==0:
                    tempword += '0'*(len(poly)-1)
                    remainder = helper.divide(tempword, poly)
                    remainder = remainder[len(remainder)-(len(poly)-1):]
                    tempword = tempword[:tempsize]
                    tempword += remainder
                    self.codewords.append(tempword)
                    tempword = ""
                tempword += packet[i]
                
        tempword += '0'*(len(poly)-1)
        remainder = helper.divide(tempword, poly)
        remainder = remainder[len(remainder)-(len(poly)-1):]
        tempword = tempword[:tempsize]
        tempword += remainder
        self.codewords.append(tempword)	