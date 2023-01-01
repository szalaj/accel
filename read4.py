import matplotlib.pyplot as plt
import numpy as np
import socket, errno, time
import matplotlib.pyplot as plt
import datetime
import psycopg2


UDP_IP = "192.168.0.3"
UDP_PORT = 5005

print('start')
conn = psycopg2.connect(dbname="postgres", user="postgres", password="Robak123", host="localhost", port=5432)

cur = conn.cursor()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
#sock.setblocking(False)



for i in range(200):
    try:
        data, addr = sock.recvfrom(1024) 

        dataraw = data.decode('utf-8').split(',')

        ts = datetime.datetime.now()
        ax = dataraw[2].strip()
        ay = dataraw[3].strip()
        az = dataraw[4].strip()

        cur.execute("INSERT INTO accel (ts, ax, ay, az) VALUES (%s, %s, %s, %s)", (ts, ax, ay, az))
        
        log = "ax: {} , ay: {} , az: {}".format(ax,ay,az)
        print(log)
       
        

    except socket.error as e:
        if e.args[0] == errno.EWOULDBLOCK: 
            print('no data')
        else:
            print(e)
            break
    
conn.commit()

cur.close()
conn.close()