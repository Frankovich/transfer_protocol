import socket  
import droneConfig as dc
from time import sleep  
from drone import Drone
import base64

d = Drone()
host = dc.coordTransfer['ip']
port = dc.coordTransfer['port']

def connect(host, port):
    
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
            payload = d.statusExample()

            clientSocket.sendall(bytes(payload, "UTF-8"))

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
