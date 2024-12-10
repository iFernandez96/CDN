import socket

HOST = "localhost"  # todo: specify the server's hostname or IP address inside the quotes
PORT = 20010 # IP of the load balancer

def send_message(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((HOST, PORT))
        byte_msg = msg.encode('utf-8')
        s.sendall(byte_msg)
        data = s.recv(1024)
        print("Received: {}".format(data.decode('utf-8')))

def main():
    file = ''
    while (file != 'done'):
        print("----------------------------------------")
        print("\tPlease enter a file to lookup!")
        print()
        print("----------------------------------------")
        file = input('')
        send_message(file)


if __name__ == "__main__":
    main()
    