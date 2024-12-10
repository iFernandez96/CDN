import socket

HOST = ""  # todo: specify the server's hostname or IP address inside the quotes
PORT1 = 20001 
PORT2 = 20002 
PORT3 = 20003 

def main():
    msg = ""
    while msg != "done":
        msg = input("Press Enter to send a message to the server\n")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((HOST, PORT))
            byte_msg = msg.encode('utf-8')
            s.sendall(byte_msg)
            data = s.recv(1024)

        print("Received: {}".format(data.decode('utf-8')))

if __name__ == "__main__":
    main()