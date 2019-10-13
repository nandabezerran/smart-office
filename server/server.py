#!flask/bin/python
import socket
import json
from flask import Flask, request, jsonify
import collections
import json
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

devices = []


@app.route('/', methods=['GET'])
def hello_world():
    teste = jsonify({"teste":"cu"})
    print(type(teste))
    return teste


@app.route('/getDevices', methods=['GET'])
def get_devices():
    resultado = []
    for device in devices:
        dev = device
        # dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
        resultado.append(dev)
    # return json.dumps(resultado, separators=(',', ':'))
    return jsonify(resultado)


@app.route('/changeStatus/<string:id>/<string:new_status>', methods=["PUT"])
def change_status(id, new_status):
    dev = None
    # print(new_status)
    for device in devices:
        if(device['id'] == id):
            # print(device["acoes"])
            device["acoes"]["status"] = str(new_status)
            dev = device
            dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
    return json.dumps(dev, separators=(',', ':'))
#   Atualizar status do device
#   sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#   sock.sendto(jsonify(resultList), (device.ip, device.port))


@app.route('/changeTemp/<string:id>/<string:new_temp>', methods=["PUT"])
def change_temperatura(id, new_temp):
    dev = None
    # print(new_status)
    for device in devices:
        if(device['id'] == id):
            # print(device["acoes"])
            device["acoes"]["temperatura"] = str(new_temp)
            dev = device
            dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
    return json.dumps(dev, separators=(',', ':'))
#   Atualizar status do device
#   sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#   sock.sendto(jsonify(resultList), (device.ip, device.port))


@app.route('/changeCanal/<string:id>/<string:new_canal>', methods=["PUT"])
def change_canal(id, new_canal):
    dev = None
    # print(new_status)
    for device in devices:
        if(device['id'] == id):
            # print(device["acoes"])
            device["acoes"]["status"] = str(new_canal)
            dev = device
            dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
    return json.dumps(dev, separators=(',', ':'))
#   Atualizar status do device
#   sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#   sock.sendto(jsonify(resultList), (device.ip, device.port))


@app.route('/changeVolume/<string:id>/<string:new_volume>', methods=["PUT"])
def change_volume(id, new_volume):
    dev = None
    # print(new_status)
    for device in devices:
        if(device['id'] == id):
            # print(device["acoes"])
            device["acoes"]["volume"] = str(new_volume)
            dev = device
            dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
    return json.dumps(dev, separators=(',', ':'))
#   Atualizar status do device
#   sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
#   sock.sendto(jsonify(resultList), (device.ip, device.port))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)


def decode_json(msg):
    device = json.loads(msg)
    devices.append(device)


server_ip = socket.gethostbyname(socket.gethostname())
server_port = 3000
server_addr = (server_ip, int(server_port))

broadcast_ip = '255.255.255.255'
broadcast_port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

broacast_addr = (broadcast_ip, broadcast_port)

sock.bind(server_addr)

msg = "Solicitando conexao..."

try:

    sock.sendto(msg.encode(), broacast_addr)

    while True:
        data, client = sock.recvfrom(1024)
        decode_json(data.decode())
        print(devices[0])

finally:
	sock.close()



