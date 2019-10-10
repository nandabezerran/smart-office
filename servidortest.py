import socket
import sys


host = ''


port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
s.bind((host, port))
    
while True:
	print('waiting to receive message')
	data, address = s.recvfrom(1024)
		
	print 'received: ' + data + '\nfrom: ' + address[0] + '\nlistening on port: ' + str(address[1])

