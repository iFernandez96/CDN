import socket

HOST = ""  # todo: specify the correct hostname of IP address to communicate with the server.
PORT = 20010 # todo: specify the correct port number to communicate with the server.
CLIENT_PORTS = [20001, 20002, 20003]

import socket


def send_message(msg, port, res = False):
    data = b""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        byte_msg = msg.encode('utf-8')
        s.sendto(byte_msg, (HOST, port))
        if res:
            data, _ = s.recvfrom(1024)
    
    return data.decode('utf-8')


def check_load(message, port):
    msg = 'check_load' + ' ' + message
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(msg.encode('utf-8'), (HOST, port))
        data, _ = s.recvfrom(1024)
    load, cache = data.decode('utf-8').split(" ")
    return int(load), cache

def main():
    # open a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Load Balancer Server listening on {}:{}'.format(HOST, PORT))
        while True:
            data, addr = s.recvfrom(1024)
            message = data.decode()
            print(f"Message recieved from Client: {message}")
            print("Looking for an edge server who either has the requested data in Cache or the least amount of load")
            if not data:
                break
            least_load = 999
            best_port = CLIENT_PORTS[0]
            for port in CLIENT_PORTS:
                load, cache = check_load(message, port)
                if load < least_load:
                    least_load = load 
                    best_port = port
                if cache == "yes":
                    best_port = port
                    break
            print(f"Found the best edge server: {HOST}:{best_port}")
            msg = send_message(message, best_port, True)
            print(f"Load Balancer recieved: {msg}")
            send_message(msg, addr[1])




if __name__ == "__main__":
    main()