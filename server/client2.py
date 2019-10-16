import socket
import json
host = socket.gethostbyname(socket.gethostname())
port_broadcast = 5000
port_client = 2000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
addr = (host, int(port_broadcast))
x = {"tipo": "lampada", "ip": host, "id": "2", "porta": port_client,
     "acoes": {"status": "Ligado"}}

client.bind((host, port_broadcast))

while True:
    print('Esperando conexão...')
    rsp, server = client.recvfrom(1024)
    print(rsp.decode() + " ---> "+ str(server[0]) + ", " + str(server[1]))
    client.close()
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((host, port_client))
    client.sendto(json.dumps(x).encode(), server)
    rsp, server = client.recvfrom(1024)
    print(rsp)
