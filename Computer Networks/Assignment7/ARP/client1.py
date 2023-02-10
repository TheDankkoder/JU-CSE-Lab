import socket
from _thread import *

host = '127.0.0.1'
port = 5000
logicalAddr = 1000
cache = {}

def receive_thread(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        if(data[0] == '0'):
            if(int(data[1:]) == logicalAddr):
                print("Physical Address Requested...")
                message = "1" + str(logicalAddr) + str(host)
                sock.sendto(message.encode(), addr)
                print("Physical Address sent to: ", addr)
        if(data[0] == '1'):
            print("Received Physical Address: ", data[5:])
            cache[int(data[1:5])] = data[5:]    
        if(data[0] == '2'):
            print("Data Received from: ", addr)
            print("Data: ", data[1:])

def send_thread(sock):
    while True:
        command = int(input("Do you want to send data? : "))
        if command == 0:
            data = input("Enter Data to send: ")
            addr = int(input("Enter IP Address: "))
            if addr in cache:
                pass
            else:
                print("Broadcasting to search for physical address...")
                message = "0" + str(addr)
                sock.sendto(message.encode(), ("255.255.255.255", 5000))
            flag = 0
            while True:
                flag = flag + 1
                if addr in cache or flag > 10000000:
                    break
            
            if flag > 10000000:
                print("Address Not Found!")
            else:
                message = "2" + data
                sock.sendto(message.encode(), (cache[addr], 5000)) 
                print("Data Sent!") 
                print(cache)

            

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((host, port))
print("Client Started...")
print("Logical Address: ", logicalAddr)
print("Physical Address: ", host)

start_new_thread(receive_thread, (sock,))
start_new_thread(send_thread, (sock,))

while True:
    pass