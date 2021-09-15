import socket

UDP_IP = "192.168.43.237"
UDP_PORT = 6677

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
 
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    # print("received message: %s" % data)
    string = str(data)
    print(string[2:len(string)-1])
    