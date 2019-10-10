import socket
import sys


host = 'localhost'

port = 1234


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print 'Para sair use CTRL+X e pressione enter\n'
msg = raw_input()

while msg <> '\x18':
	#envia os dados
	s.sendto(msg, (host, port))
	
	msg = raw_input()
	
print('closing socket')
s.close()