import socket

HOST = ""  # todo: specify the correct hostname of IP address to communicate with the server.
PORT = 20040# todo: specify the correct port number to communicate with the server.
STORAGE = {
    "file1": "This is File 1", 
    "file2": "This is File 2", 
    "file3": "This if File 3",
    "file4": "This if File 4",
    "file5": "This is File 5", 
    "file6": "This is File 6", 
    "file7": "This if File 7",
    "file8": "This if File 8"
    }

# open a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('Server listening on {}:{}'.format(HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        # s.sendto(data.upper(), addr)
        if data.decode() in STORAGE:
            print(f"Data found! Sending data to client: {STORAGE[data.decode()]}")
            s.sendto(STORAGE[data.decode()].encode(), addr)
        else:
            msg = "CannotFind"
            s.sendto(msg.encode(), addr)
