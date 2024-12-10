import socket

HOST = ""  # todo: specify the correct hostname of IP address to communicate with the server.
PORT = 20040# todo: specify the correct port number to communicate with the server.


# open a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('Server listening on {}:{}'.format(HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        s.sendto(data.upper(), addr)
