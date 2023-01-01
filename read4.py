import matplotlib.pyplot as plt
import numpy as np
import socket, errno, time
import matplotlib.pyplot as plt
import datetime


UDP_IP = "192.168.0.3"
UDP_PORT = 5005

print('start')
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
#sock.setblocking(False)



for i in range(200):
    try:
        data, addr = sock.recvfrom(1024) 

        dataraw = data.decode('utf-8').split(',')

        ax = dataraw[2].strip()
        ay = dataraw[3].strip()
        az = dataraw[4].strip()
        
        log = "ax: {} , ay: {} , az: {}".format(ax,ay,az)
        print(log)
       
        

    except socket.error as e:
        if e.args[0] == errno.EWOULDBLOCK: 
            print('no data')
        else:
            print(e)
            break
    
