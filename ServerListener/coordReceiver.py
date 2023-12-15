import socket
import receiverConfig as rc
from time import sleep
import base64
from PIL import Image
from datetime import datetime
import re

host = rc.coordReceiver['ip']
port = rc.coordReceiver['port']

def startListener(host, port, commRate = 1):
    serverSocket = socket.socket()
    serverSocket.bind((host, port))  
    serverSocket.listen(5)  
    con, addr = serverSocket.accept()  
    buffersize = 1024
    dt_string = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
    filename = "./db/coordinates/" + re.sub("[/_:]", "-", dt_string) 
    f = open(filename, "w")
    f.write(dt_string + '\n')
    f.close()
    while True:
        try:
            con.send( bytes("Ping from server", "UTF-8")) 
            data = con.recv(buffersize).decode()

            f = open(filename, "a")
            f.write(data + " —— " + datetime.now().strftime("%d/%m/%Y_%H:%M:%S") + "\n")
            f.close()
            
            print(data)
            
        except socket.error:
            print(socket.error)
            print("Unable to receive coords...")
            serverSocket.close()
            break
        sleep(commRate)  
    con.close()

while True:
    startListener(host, port)