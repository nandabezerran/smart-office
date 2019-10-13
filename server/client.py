import socket
host = socket.gethostbyname(socket.gethostname())
server_ip = socket.gethostbyname(socket.gethostname())
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
addr = (host, int(port))
msgF = "nANDINHA"
client.bind((server_ip, port))

while True:
    msg = input("Servidor 1")
    rsp, server = client.recvfrom(1024)
    print(rsp)
    print(server)
    client.sendto(msgF.encode(), server)

