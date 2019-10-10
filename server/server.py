#!flask/bin/python
import socket
import device_pb2 
from flask import Flask
from flask import jsonify

app = Flask(__name__)

# The connection with the client will be made with the flask routes, not by the pure TCP socket.
# The sockets here are only for the connections with the dispositives that are made with UDP

dispositives = []
host = ''
port = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origUdp = (host, port)
udp.bind(origUdp)

while True:
	print ("Listening")

    msg, disp = udp.recvfrom(1024) # Gets the IP of the dispositive
    msg = msg.decode() # Gets info from the dispositive
    msg.ParseFromString(msg) # Parse the protobuf binary message
	dispositive.append(msg); # Add the dispositive to the vector