import socket
from flask import Flask, request, jsonify
import collections
from threading import Timer
import json
#from flask_cors import CORS
import copy 
app = Flask(__name__)
#CORS(app)

devices = []

@app.route('/getDevices', methods=['GET'])
def get_devices():
    resultado = []
    for device in devices:
        dev = device
        resultado.append(dev)
    return jsonify(resultado)


@app.route('/changeStatus/<string:id>/<string:new_status>', methods=["PUT"])
def change_status(id, new_status):
    dev = None
    for device in devices:
        if(int(device['id']) == int(id)):
            device["acoes"]["status"] = str(new_status)
            sock.sendto(json.dumps(device).encode(), (device['ip'], int(device['porta'])))
            return json.dumps(device, separators=(',', ':'))
    return 'Dispositivo nao encontrado', 502


@app.route('/changeTemp/<string:id>/<string:new_temp>', methods=["PUT"])
def change_temperatura(id, new_temp):
    dev = None
    for device in devices:
        if(int(device['id']) == int(id)):
            device["acoes"]["temperatura"] = int(new_temp)
            sock.sendto(json.dumps(device).encode(), (device['ip'], int(device['porta'])))
            return json.dumps(device, separators=(',', ':'))
    return 'Dispositivo nao encontrado', 502

@app.route('/changeCanal/<string:id>/<string:new_canal>', methods=["PUT"])
def change_canal(id, new_canal):
    dev = None
    for device in devices:
        if(int(device['id']) == int(id)):
            device["acoes"]["canal"] = int(new_canal)
            sock.sendto(json.dumps(device).encode(), (device['ip'], int(device['porta'])))
            return json.dumps(device, separators=(',', ':'))
    return 'Dispositivo nao encontrado', 502


@app.route('/changeVolume/<string:id>/<string:new_volume>', methods=["PUT"])
def change_volume(id, new_volume):
    dev = None
    for device in devices:
        if(int(device['id']) == int(id)):
            device["acoes"]["volume"] = int(new_volume)
            sock.sendto(json.dumps(device).encode(), (device['ip'], int(device['porta'])))
            return json.dumps(device, separators=(',', ':'))
    return 'Dispositivo nao encontrado',502


if __name__ == '__main__':
    def decode_json(msg):
        device = json.loads(msg)
        for i in range (0, len(devices)):
            if (devices[i]['id'] == device['id']):
                devices[i] = copy.copy(device)
                return
        devices.append(device)

    app.run(host='127.0.0.1', port='2000', debug=True)
    server_ip = socket.gethostbyname(socket.gethostname())
    server_port = 3000
    server_addr = (server_ip, int(server_port))

    broadcast_ip = '255.255.255.255'
    broadcast_port = 5000

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    broacast_addr = (broadcast_ip, broadcast_port)

    sock.bind(server_addr)

    msg = 'Aguardando Conexao...'

    def send_broadcast():
        print("enviou")
        sock.sendto(msg.encode(), broacast_addr)

    while True:
        # ------------ RECEIVE TO DEVICE
        t = Timer(2.0, send_broadcast)
        t.start()
        data, client = sock.recvfrom(1024)
        client_server = data.decode("utf-8").replace("'", '"')
        client_data = data.decode("utf-8").replace("'", '"')
        decode_json(client_data)








