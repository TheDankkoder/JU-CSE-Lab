import socket
from _thread import *

host = '127.0.0.1'
port = 5000
server_addr = 1
start_address = 1000
end_address = 2000
curr_address = start_address
cache = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((host, port))
print("Server Started...")

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode()
    data = data.split(" ")
    if(data[0] == 'DHCPDISCOVER'):
        print('Received DHCP discover from: ', addr)
        message = 'DHCPOFFER' + ' ' + str(host) + ' ' + str(curr_address) 
        sock.sendto(message.encode(), addr)
        print('DHCP offer sent to: ', addr)
    if(data[0] == 'DHCPREQUEST'):
        print('Received DHCP request from: ', addr)
        if data[1] == host:
            message = 'DHCPACK'
            sock.sendto(message.encode(), addr)
            curr_address = curr_address + 1
            print('Sending DHCP acknowledgement...')
        else:
            print('DHCP offer rejected!')