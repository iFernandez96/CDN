import socket

HOST = ""  
PORT = 20001
DB_PORT = 20040
LOAD = 80
CACHE = {"file1": "This is File 1", "file2": "This is File 2"} #YES DOES EXIST IN CACHE

SERVER_NUM = 1

def send_message(msg, port, res = False):
    data = b""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        byte_msg = msg.encode('utf-8')
        s.sendto(byte_msg, (HOST, port))
        if res:
            data, _ = s.recvfrom(1024)
    
    return data.decode('utf-8')



# open a UDP socket
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f'[{SERVER_NUM}] - listening on {HOST}:{PORT}')
        while True:
            data, addr = s.recvfrom(1024)
            if not data:
                break
            recieved = data.decode().split(" ")
            print()
            print(f"[{SERVER_NUM}] - recieved {recieved}")
            if (recieved[0] == "check_load"):
                print(f'[{SERVER_NUM}] - pinged for load check')
                in_cache = "yes"
                if recieved[1] not in CACHE:
                    in_cache = "no"
                message_back = str(LOAD) + " " + in_cache
                send_message(message_back, addr[1])
            else:
                if recieved[0] not in CACHE:
                    msg = send_message(recieved[0], DB_PORT, True)
                    print(f"[{SERVER_NUM}] - msg recieved from database: {msg}")
                    send_message(msg, addr[1])
                else: 
                    print(f"[{SERVER_NUM}] - Found in CACHE")
                    send_message(CACHE[recieved[0]], addr[1])
            
if __name__ == '__main__':
    main()
