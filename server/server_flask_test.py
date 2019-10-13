from flask import Flask, request, jsonify
import collections
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
devices = [{
        "tipo": "Ar-condicionado",
        "ip": "adosihdaiosddios",
        "id": "1",
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
            "temperatura": 30,
        }
    },{
        "tipo": "TV",
        "ip": "adosihdaiosddios",
        "id": "2",
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
            "canal": 30,
            "volume": 20
        }
    },{
        "tipo": "Lâmpada",
        "ip": "adosihdaiosddios",
        "id": "3",
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
        }
    },{
        "tipo": "Lâmpada",
        "ip": "adosihdaiosddios",
        "id": "5",
        "porta": 3000,
        "acoes": {
            "status": "Desligado"
        }
    }]

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