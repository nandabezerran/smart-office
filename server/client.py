import socket
import json
host = socket.gethostbyname(socket.gethostname())
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
addr = (host, int(port))
x = {"tipo": "Ar-condicionado", "ip": host, "id": "1", "porta": port,
     "acoes": {"status": "Ligado",
               "temperatura": 30}}

client.bind((host, port))

while True:
    print('Esperando conexão...')
    rsp, server = client.recvfrom(1024)
    print(rsp.decode() + " ---> "+ str(server[0]) + ", " + str(server[1]))
    client.sendto(json.dumps(x).encode(), server)

