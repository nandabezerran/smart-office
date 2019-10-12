import socket
host = socket.gethostbyname(socket.gethostname())
port = 9434

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (host, int(port))
msg = "nANDINHA"

while True:
    msg = input("Deu bom!!")
    rsp, server = client.recvfrom(4096)
    print(rsp)
    print(server)
    client.sendto(msg.encode(), server)

