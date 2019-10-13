#!flask/bin/python
import socket
# from flask import Flask
# from flask import jsonify
# import collections

# app = Flask(__name__)
#
# devices = []
#
# @app.route('/server/<string:id>/<string:status>', methods=['PUT'])
# def changeStatus(id, status):
#     resultList = []
#     for device in devices:
#         if(device.id == "id"):
#             dp = collections.OrderedDict()
#             dp = {'status': status}
#             resultList.append(dp)
#
#             device.status = status
#
#             sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#             sock.sendto(jsonify(resultList), (device.ip, device.port))
#
# @app.route('/server/getDevices', methods=['GET'])
# def getDevices(id, status):
#     resultList = []
#     for device in devices:
#         # Mudar para protoBuffers
#         dp = collections.OrderedDict()
#         dp = {'id':device.id, 'status': device.status, 'acoes': jsonify(device.acoes)}
#         resultList.append(dp)
#     return jsonify(resultList)
#
# @app.route('/server/changeVolume/<string:volume>', methods=['PUT'])
# def changeTvVolume(volume):
#     resultList = []
#     for device in devices:
#         if(device.id == "tv"):
#             dp = collections.OrderedDict()
#             dp = {'volume': volume}
#             resultList.append(dp)
#
#             device.acoes.volume = volume
#
#             sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#             sock.sendto(jsonify(resultList), (device.ip, device.port))
#
# @app.route('/server/changeChannel/<string:channel>', methods=['PUT'])
# def changeTvChannel(channel):
#     resultList = []
#     for device in devices:
#         if(device.id == "tv"):
#             dp = collections.OrderedDict()
#             dp = {'canal': channel}
#             resultList.append(dp)
#
#             device.acoes.canal = channel
#
#             sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#             sock.sendto(jsonify(resultList), (device.ip, device.port))
#
# @app.route('/server/changeAirTemp/<string:temp>', methods=['PUT'])
# def changeAirTemp(temp):
#     resultList = []
#     for device in devices:
#         if(device.id == "ar-condicionado"):
#             dp = collections.OrderedDict()
#             dp = {'temperatura': temp}
#             resultList.append(dp)
#
#             device.acoes.temperatura = temp
#
#             sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#             sock.sendto(jsonify(resultList), (device.ip, device.port))

# The connection with the client will be made with the flask routes, not by the pure TCP socket.
# The sockets here are only for the connections with the dispositives that are made with UDP
server_ip = socket.gethostbyname(socket.gethostname())
server_port = 3000
server_addr = (server_ip, int(server_port))

host_broadcast = '255.255.255.255'
port_broadcast = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.settimeout(5)

broacast_addr = (host_broadcast, port_broadcast)

sock.bind(server_addr)
print("server criado")

msg = "ssssss"

try:

    sock.sendto(msg.encode(), broacast_addr)

    while True:
        print("etrou")
        data, client = sock.recvfrom(1024)
        print(data)
        print(client)
        sock.sendto(msg.encode(), client)

finally:
	sock.close()

# while True:
# 	print ("Listening")
#
#     msg, disp = udp.recvfrom(1024) # Gets the IP of the dispositive
    # msg = msg.decode() # Gets info from the dispositive
    # msg.ParseFromString(msg) # Parse the protobuf binary message
	# dispositive.append(msg); # Add the dispositive to the vector