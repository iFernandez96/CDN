import socket

HOST = ""  # todo: specify the correct hostname of IP address to communicate with the server.
PORT = 20010 # todo: specify the correct port number to communicate with the server.
CLIENT_PORTS = [20001, 20002, 20003]

def send_message(msg, port):
    data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((HOST, port))
        byte_msg = msg.encode('utf-8')
        s.sendall(byte_msg)
        data += s.recv(1024)
    
    return data

def check_load(port):
    msg = 'check_load'
    data = ""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((HOST, port))
        byte_msg = msg.encode('utf-8')
        s.sendall(byte_msg)
        data += s.recv(1024)
    load, cache = data.split(" ")
    return load, cache

def main():
    # open a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Load Balancer Server listening on {}:{}'.format(HOST, PORT))
        while True:
            data, addr = s.recvfrom(1024)
            if not data:
                break
            least_load = 999
            best_port = CLIENT_PORTS[0]
            for port in CLIENT_PORTS:
                load, cache = check_load(port)
                if load < least_load:
                    least_load = load 
                    best_port = port
                if cache:
                    best_port = port
                    break

            send_message(data, best_port)




if __name__ == "__main__":
    main()