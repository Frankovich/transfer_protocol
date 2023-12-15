import socket  
import droneConfig as dc
from time import sleep  
from drone import Drone
import base64

d = Drone()
host = dc.imageTransfer['ip']
port = dc.imageTransfer['port']
image = "Thresher.jpg"

def connect(host = "xxxx", port = 8080):
    
    clientSocket = socket.socket() 
    connected = False  
    while connected == False:
        try: 
            clientSocket.connect((host, port))  
            connected = True  
            print("Connection established")
        except socket.error:  
            print("Failed to connect")
            sleep(3)

    while True:  
        try:  
            myfile = open(image, 'rb')
            payload = myfile.read()
            size = len(payload)
            print(size)

            clientSocket.sendall(payload)

            message = clientSocket.recv( 1024 ).decode( "UTF-8" )  
            print( message )  
        except socket.error:  
            connected = False  
            print("connection lost... reconnecting")  
            clientSocket.close()
            break
    
    clientSocket.close()
    
while True:
    connect(host, port)
