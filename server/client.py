import socket
import json
host = socket.gethostbyname(socket.gethostname())
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
addr = (host, int(port))
x = {"tipo": "Ar-condicionado", "ip": "adosihdaiosddios", "id": "1", "porta": 5000,
     "acoes": {"status": "Ligado",
               "temperatura": 30}}

client.bind((host, port))

while True:
    msg = input("Servidor 1")
    rsp, server = client.recvfrom(1024)
    print(rsp)
    print(server)
    client.sendto(json.dumps(x).encode(), server)

