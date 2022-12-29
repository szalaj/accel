import socket
from datetime import datetime
import matplotlib.pyplot as plt
import random
import time
import threading

UDP_IP = "192.168.0.3"
UDP_PORT = 5005

print('start')
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

dane = []

# This just simulates reading from a socket.
def data_listener():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        ys = (data.decode('ASCII').split(',')[2]).strip()
        print(ys)
        dane.append(float(ys))

if __name__ == '__main__':
    thread = threading.Thread(target=data_listener)
    thread.daemon = True
    thread.start()
    #
    # initialize figure
    plt.figure() 
    ln, = plt.plot([])
    plt.ion()
    plt.show(block=False)
    while True:
        print(len(dane))
        ln.set_xdata(range(len(dane)))
        ln.set_ydata(dane)
        plt.draw()
