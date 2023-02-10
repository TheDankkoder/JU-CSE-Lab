import socket
import sys
import time
import util
import helper
	
def Main(senderno):
	count = 0
	sentframes = []
	print('Starting Sender #',senderno)
	host = '127.0.0.1'
	port = 8080
	
	mySocket = socket.socket()
	mySocket.connect((host, port))
	
	while True:
		print()
		data = input("Enter $ ")
		data = helper.createFrame(data) + '/' + str(count) + '/'
		msg = helper.extractMessage(data)
		print('Sending to channel :',str(msg))
		mySocket.send(data.encode())
		sentframes.append(data)
		count += 1
		
		if not msg:
			break
		if msg == 'exit0':
			break
		
	mySocket.close()
	
if __name__ == '__main__':
	if len(sys.argv) > 1:
		senderno = int(sys.argv[1])
	else:
		senderno = 1
	Main(senderno)
	
		