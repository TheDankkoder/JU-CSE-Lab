import socket
from _thread import *
import time

host = '127.0.0.3'
port = 5000
IP = ""
IP_server = ""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((host, port))
print("Client Started...")

while True:
    if IP:
        print("Client Ready!")
        time.sleep(5)
        IP = ""
        print("IP reinitialization required!")
    else:
        print("Initiating DHCP...")
        if IP_server:
            message = "DHCPDISCOVER" + ' ' + str(host)
            sock.sendto(message.encode(), IP_server)
            
            while True:
                if IP:
                    break
                data, addr = sock.recvfrom(1024)
                data = data.decode()
                data = data.split(" ")
                temp_IP = ""
                temp_IP_server = ""
                if(data[0] == 'DHCPOFFER'):
                    temp_IP = data[2]
                    temp_IP_server = data[1]
                    print("DHCP offer received from: ", addr)
                    print("Sending DHCP request...")
                    message = 'DHCPREQUEST' + ' ' + data[1]
                    sock.sendto(message.encode(), IP_server)
                    while True:
                        data, addr = sock.recvfrom(1024)
                        data = data.decode()
                        data = data.split(" ")
                        if(data[0] == 'DHCPACK'):
                            print("Received acknowledgement!")
                            print("Assigned IP: ", temp_IP)
                            IP = temp_IP
                            IP_server = addr
                            break
        else:
            message = "DHCPDISCOVER" + ' ' + str(host)
            sock.sendto(message.encode(), ('255.255.255.255', port))
            
            while True:
                if IP:
                    break
                data, addr = sock.recvfrom(1024)
                data = data.decode()
                data = data.split(" ")
                temp_IP = ""
                temp_IP_server = ""
                if(data[0] == 'DHCPOFFER'):
                    temp_IP = data[2]
                    temp_IP_server = data[1]
                    print("DHCP offer received from: ", addr)
                    print("Sending DHCP request...")
                    message = 'DHCPREQUEST' + ' ' + data[1]
                    sock.sendto(message.encode(), ("255.255.255.255", port))
                    while True:
                        data, addr = sock.recvfrom(1024)
                        data = data.decode()
                        data = data.split(" ")
                        if(data[0] == 'DHCPACK'):
                            print("Received acknowledgement!")
                            print("Assigned IP: ", temp_IP)
                            IP = temp_IP
                            IP_server = addr
                            break
                    