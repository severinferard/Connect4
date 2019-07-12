import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 2000

server_ip = socket.gethostbyname(server)

try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for connections")

current_player = "1"
info = "0"

def threaded_client(conn):
    global info, clients, current_player
    data = "Connected"
    conn.send(str.encode(current_player))
    current_player = "2"
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                print("break")
                break
            elif reply == "request":
                conn.send(str.encode(str(info)))

            elif reply == "n_connected":
                conn.send(str.encode(str(len(clients))))

            else:
                print("Received" + reply)
                conn.sendall(str.encode(reply))
                info = reply
        except:
            break
    current_player = "1"
    info = "0"
    print("Connection closed")
    conn.close()
    clients.remove(conn)

clients = []

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print("Connected to", addr)
    start_new_thread(threaded_client, (conn,))
