import socket
import os

HOST = "localhost"  # todo: specify the server's hostname or IP address inside the quotes
PORT = 20010 # IP of the load balancer

def send_message(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        byte_msg = msg.encode('utf-8')
        s.sendto(byte_msg, (HOST, PORT))
        data = s.recv(1024)
        print(f"Received: {data.decode()}")

def main():
    file = ''
    os.system("clear")
    while (file != 'done'):
        print("--------------------------------------------------")
        print("\tPlease enter a file to lookup!")
        print()
        print("--------------------------------------------------")
        file = input('')
        send_message(file)
        print()
        print()
        print()
        print()
        print()
        print()
        print("please press enter to clear the screen for the next query...")
        user_input = input('')
        if user_input == "":
            os.system("clear")


if __name__ == "__main__":
    main()
    