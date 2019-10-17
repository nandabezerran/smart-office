#!flask/bin/python
import socket
from flask import Flask, request, jsonify
import collections
from threading import Timer
import json
from flask_cors import CORS
import copy 
from device_pb2 import Device, DeviceList

app = Flask(__name__)
CORS(app)

_devices = [{
        "tipo": "Ar-condicionado",
        "ip": "adosihdaiosddios",
        "id": 1,
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
            "temperatura": 30,
        }
    },{
        "tipo": "TV",
        "ip": "adosihdaiosddios",
        "id": 2,
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
            "canal": 30,
            "volume": 20
        }
    },{
        "tipo": "Lâmpada",
        "ip": "adosihdaiosddios",
        "id": 3,
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
        }
    },{
        "tipo": "Lâmpada",
        "ip": "adosihdaiosddios",
        "id": 4,
        "porta": 3000,
        "acoes": {
            "status": "Desligado"
        }
    }]




@app.route('/getDevices', methods=['GET'])
def get_devices():
    resultado = DeviceList()
    i = 0
    for device in _devices:
        dev = resultado.devices.add()
        dev.ip = device['ip']
        dev.id = device['id']
        dev.port = device['porta']
        dev.status = device['acoes']['status']
        dev.tipo = device['tipo']

        if(device['tipo'] == 'TV'):
            dev.channel = device['acoes']['canal']
            dev.volume = device['acoes']['volume']
        if(device['tipo'] == 'Ar-condicionado'):
            dev.temperature = device['acoes']['temperatura']
    #     devices = DeviceList()
    # device = devices.devices.add()
    # device.id = json_response_device['id']
    # device.tipo = json_response_device['tipo']
    # device.ip = json_response_device['ip']
    # device.port = json_response_device['porta']
    # device.status = json_response_device['status']

    # if(json_response_device[0]['tipo'] == 'Ar-condicionado'){
    #     device.temperatura = json_response_device['temperatura']
    # } else if(json_response_device[0]['tipo'] == 'TV'){
    #     device.canal = json_response_device['canal']
    #     device.volume = json_response_device['volume']
    # }
    return resultado.SerializeToString()


@app.route('/changeStatus/<string:id>/<string:new_status>', methods=["PUT"])
def change_status(id, new_status):
    dev = Device();
    for device in _devices:
        if(device['id'] == id):
            device["acoes"]["status"] = str(new_status)
            dev.ip = device['ip']
            dev.id = device['id']
            dev.port = device['porta']
            dev.status = device['acoes']['status']
            dev.tipo = device['tipo']

            if(device['tipo'] == 'Ar-condicionado'):
                dev.temperature = ['acoes']['temperatura']
            if(device['tipo'] == 'TV'):
                dev.channel = device['acoes']['canal']
                dev.volume = device['acoes']['volume']
            # dev[] = json.dumps(dev['acoes'], separators=(',', ':'))
            # sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
            # sock.sendto(json.dumps(dev).encode(), (device['ip'], device['porta']))
    # return json.dumps(dev, separators=(',', ':'))
    return dev.SerializeToString()


@app.route('/changeTemp/<string:id>/<string:new_temp>', methods=["PUT"])
def change_temperatura(id, new_temp):
    dev = Device()
    for device in devices:
        if(device['id'] == id):
            device["acoes"]["temperatura"] = str(new_temp)
            dev.ip = device['ip']
            dev.id = device['id']
            dev.port = device['porta']
            dev.status = device['acoes']['status']
            dev.tipo = device['tipo']

            if(device['tipo'] == 'Ar-condicionado'):
                dev.temperature = ['acoes']['temperatura']
            if(device['tipo'] == 'TV'):
                dev.channel = device['acoes']['canal']
                dev.volume = device['acoes']['volume']
            # sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
            # sock.sendto(json.dumps(dev).encode(), (device['ip'], device['porta']))
    return dev.SerializeToString()

@app.route('/changeCanal/<string:id>/<string:new_canal>', methods=["PUT"])
def change_canal(id, new_canal):
    dev = Device()
    for device in devices:
        if(device['id'] == id):
            device["acoes"]["canal"] = str(new_canal)
            dev.ip = device['ip']
            dev.id = device['id']
            dev.port = device['porta']
            dev.status = device['acoes']['status']
            dev.tipo = device['tipo']

            if(device['tipo'] == 'Ar-condicionado'):
                dev.temperature = ['acoes']['temperatura']
            if(device['tipo'] == 'TV'):
                dev.channel = device['acoes']['canal']
                dev.volume = device['acoes']['volume']
            
            # dev = copy.copy(device)
            # dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
            # sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
            # sock.sendto(json.dumps(dev).encode(), (device['ip'], device['porta']))
    # return json.dumps(dev, separators=(',', ':'))
    return dev.SerializeToString()


@app.route('/changeVolume/<string:id>/<string:new_volume>', methods=["PUT"])
def change_volume(id, new_volume):
    dev = Device()
    for device in devices:
        if(device['id'] == id):
            device["acoes"]["volume"] = str(new_volume)
            device["acoes"]["temperatura"] = str(new_temp)
            dev.ip = device['ip']
            dev.id = device['id']
            dev.port = device['porta']
            dev.status = device['acoes']['status']
            dev.tipo = device['tipo']

            if(device['tipo'] == 'Ar-condicionado'):
                dev.temperature = ['acoes']['temperatura']
            if(device['tipo'] == 'TV'):
                dev.channel = device['acoes']['canal']
                dev.volume = device['acoes']['volume']
            # dev = copy.copy(device)
            # dev['acoes'] = json.dumps(dev['acoes'], separators=(',', ':'))
            # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # sock.sendto(json.dumps(dev).encode(), (device['ip'], device['porta']))
    # return json.dumps(dev, separators=(',', ':'))
    return dev.SerializeToString()


if __name__ == '__main__':
    def decode_json(msg):
        device = json.loads(msg)
        for dev in devices:
            if (device['ip'] == dev['ip']):
                return
        devices.append(device)

    app.run(host='127.0.0.1', port='2000', debug=True)
    devices = []
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


    def send_broadcast():
        sock.sendto(msg.encode(), broacast_addr)

    sock.sendto(msg.encode(), broacast_addr)

    while True:
        t = Timer(10.0, send_broadcast)
        t.start()
        data, client = sock.recvfrom(1024)
        decode_json(data.decode())
        print(data.decode())
        id = json.loads(data.decode())['id']
        ip = json.loads(data.decode())["ip"]
        port = json.loads(data.decode())['porta']
        print("Deu certo conectar com o cliente" + str(id) + " no endereço " + str(ip) + " , " + str(port))
        msg2 = "Conexão estabelecida na nova porta"
        sock.sendto(msg2.encode(), (json.loads(data.decode())["ip"], json.loads(data.decode())['porta']))







