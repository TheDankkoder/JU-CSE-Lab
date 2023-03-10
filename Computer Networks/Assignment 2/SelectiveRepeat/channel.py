import socket
import time
import subprocess
import random
import os 
import errorInjection
import helper


	
class Channel():
	
	def __init__(self, totalsender, totalreceiver, windowsize):
		self.totalsender = totalsender
		self.senderhost = '127.0.0.1'
		self.senderport = 8080
		self.senderconn = []
		
		self.totalreceiver = totalreceiver
		self.receiverhost = '127.0.0.2'
		self.receiverport = 9090
		self.receiverconn = []
		
		self.windowsize = windowsize
		self.slidingwindow = []
		self.currentcount = 0
		#self.statuswindow = []
		
	def initSenders(self):
		senderSocket = socket.socket()
		senderSocket.bind((self.senderhost, self.senderport))
		senderSocket.listen(self.totalsender)
		for i in range(1, self.totalsender+1):
			conn = senderSocket.accept()
			self.senderconn.append(conn)
		print('Sender connections started')
		
	def closeSenders(self):
		for conn in self.senderconn:
			conn[0].close()
		print('Sender connections closed')
		
	def initReceivers(self):
		receiverSocket = socket.socket()
		receiverSocket.bind((self.receiverhost, self.receiverport))
		receiverSocket.listen(self.totalreceiver)
		for i in range(1, self.totalreceiver+1):
			conn = receiverSocket.accept()
			self.receiverconn.append(conn)
		print('Receiver connections started')
		
	def closeReceivers(self):
		for conn in self.receiverconn:
			conn[0].close()
		print('Receiver connections closed')
			
	def processData(self):
		
		while True:
			for i in range(len(self.senderconn)):
				print()
				
				conn = self.senderconn[i]
				data = conn[0].recv(1024).decode()
				prevtime = time.time()
				data = str(data)
				origmsg = helper.extractMessage(data)
				if not origmsg:
					break
				if origmsg == 'q0':
					break
				print('Message received from Receiver',i+1,':',str(data))
				
				
				recvno = random.randint(0,len(self.receiverconn)-1) 
				print('Sending to Receiver',recvno+1)
				rconn = self.receiverconn[recvno]
				cnt = helper.extractCount(data)
				msg = errorInjection.injectRandomError(origmsg)
				newdata = msg + '/' + str(cnt) + '/'
				rconn[0].sendto(newdata.encode(), rconn[1])
				
				#received from receiver
				rdata = rconn[0].recv(1024).decode()
				rdata = str(rdata)
				time.sleep(0.5)
				curtime = time.time()
				if curtime-prevtime > 2:
					timeout = 1
					newdata += 'TIMEOUT'
				else:
					timeout = 0
					newdata += rdata
				
				self.slidingwindow.append([data, newdata, i, recvno])
				
				
				msg = helper.extractMessage(newdata)
				cnt = helper.extractCount(newdata)
				status = helper.extractStatus(newdata)
				print(msg,str(cnt),status)
				print('Round trip time: ',str(curtime-prevtime))
				print('Current frame no:',str((self.currentcount % windowsize)+1))
				if (self.currentcount % windowsize)+1 == self.windowsize:
					idx = 0
					flag = 1
					
					while flag == 1:
						idx = 0
						flag = 0
						nakframes = []
						indices = []
						while idx < self.windowsize:
							currframe = self.slidingwindow[idx][1]
							msg = helper.extractMessage(currframe)
							cnt = helper.extractCount(currframe)
							status = helper.extractStatus(currframe)
							
							if status == 'NAK' or status == 'TIMEOUT':
								flag = 1
								nakframes.append(self.slidingwindow[idx])
								indices.append(idx+1)
								#break
							idx += 1
						
						if flag==0:
							print(' ------------------------------ ')	
							print('BLOCK OF WINDOW SIZE',self.windowsize,'SUCCESSFULLY SENT')
							print(' ------------------------------ ')	
						
						idx = 0
						
						while flag == 1 and idx < len(nakframes):
							
							print()
							prevtime = time.time()
							prevframe = nakframes[idx][0]
							currframe = nakframes[idx][1]
							sendno = nakframes[idx][2]
							recvno = nakframes[idx][3]
							conn = self.senderconn[sendno]
							rconn = self.receiverconn[recvno]
							stat = helper.extractStatus(currframe)
						
							print(' ------------------------------ ')
							print('RESENDING FRAME NO:',str(indices[idx]))
							print(' ------------------------------ ')	
							#sending all frames to its sender from first NAK 							
							#conn[0].send(currframe.encode())
							
							#data = conn[0].recv(1024).decode()
							print('Current frame no:',str(indices[idx]))
							print('Again Sending to Receiver',recvno+1)
							
							msg = helper.extractMessage(prevframe)
							msg = errorInjection.injectRandomError(msg)
							data = msg + '/' + str(cnt) + '/'
							rconn[0].sendto(data.encode(), rconn[1])
							
							# receiving ACK or NAK from receiver 
							rdata = rconn[0].recv(1024).decode()
							rdata = str(rdata)
							data += rdata
							
							msg = helper.extractMessage(data)
							cnt = helper.extractCount(data)
							stat = helper.extractStatus(data)
							curtime = time.time()
							print(msg,str(cnt),stat)
							print('Round trip time: ',str(curtime-prevtime))
							self.slidingwindow[indices[idx]-1][1] = data 
							idx += 1
										
							
					
						
				
				self.currentcount += 1
			if origmsg == 'exit0':
				break
		return

if __name__ == '__main__':
	#Main()
	totalsen = 1
	print('Number of senders',totalsen)
	totalrecv = 1
	print('Number of receivers',totalrecv)
	windowsize = 4
	print('Window size:',windowsize)
	
	
	ch = Channel(totalsen, totalrecv, windowsize)
	ch.initSenders()
	ch.initReceivers()
	ch.processData()
	ch.closeSenders()
	ch.closeReceivers()		
