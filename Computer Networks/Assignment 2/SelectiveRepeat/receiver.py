import socket
import sys
import time
import random
import error
import helper

def waitRandomTime():
	x = random.randint(0,5)
	if x <= 1:
		time.sleep(2)
		

	
def Main(senderno):
	print('Starting Receiver #',senderno)
	host = '127.0.0.2'
	port = 9090
	
	mySocket = socket.socket()
	mySocket.connect((host, port))
	
	while True:
		print()
		data = mySocket.recv(1024).decode()
		data = str(data)
		msg = helper.extractMessage(data)
		if not msg:
			break
		if msg == 'exit0':
			break
		
		print('Received from channel :', str(data))
		waitRandomTime()
		if error.checkError(msg) == 0:
			rdata = 'ACK'
		else:
			rdata = 'NAK'
		
		print('Sending to channel :',str(rdata))
		mySocket.send(rdata.encode())
		
		
		
	mySocket.close()
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		senderno = int(sys.argv[1])
	else:
		senderno = 1
	Main(senderno)
	
		