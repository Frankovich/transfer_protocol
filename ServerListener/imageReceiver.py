import socket
import receiverConfig as rc
from time import sleep
import base64
from PIL import Image
from datetime import datetime
import re
import traceback # for testing, remove later

host = rc.imageReceiver['ip']
port = rc.imageReceiver['port']

def startListener(host, port, commRate = 1):
    serverSocket = socket.socket()
    serverSocket.bind((host, port))  
    serverSocket.listen(5)  
    con, addr = serverSocket.accept()  
    buffersize = 4096
    imgID = 0

    while True:
        try:

            data = con.recv(4096)
            txt = data
            #print(txt)
            if data.startswith(b'SIZE'):
                tmp = txt.split()
                size = int(tmp[1])
                print('got size')
                con.sendall("GOT SIZE".encode('UTF-8'))
            elif len(data) < 0:
                raise Exception("Received empty string")
            
            else :
                myfile = open("testImage" + str(imgID) + ".jpg", 'wb')
                imgID += 1
                myfile.write(data)

                data = con.recv(40960000)
                if not data:
                    myfile.close()
                    break
                myfile.write(data)
                myfile.close()

                con.sendall(b"GOT IMAGE")
            
        except Exception as e: 
            print(e)
            print(traceback.format_exc())
            print("Unable to receive images...")
            serverSocket.close()
            break
        sleep(commRate)  
    con.close()

while True:
    print(host, port)
    try:
        startListener(host, port)
    except Exception as e: 
        print(e)
        sleep(3)  
        print("Trying to connect...")
