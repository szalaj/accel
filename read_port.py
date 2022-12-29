import socket
import matplotlib.pyplot as plt

UDP_IP = "192.168.0.3"
UDP_PORT = 5005

print('start')
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))



circle1 = plt.Circle((0, 0), 0.2, color='r')
plt.gca().add_patch(circle1)

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    
    print(data.decode('ASCII').split(',')[2])

    plt.show()
    plt.pause(0.0001)
