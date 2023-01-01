import matplotlib.pyplot as plt
import numpy as np
import socket, errno, time
import matplotlib.pyplot as plt

UDP_IP = "192.168.0.3"
UDP_PORT = 5005

print('start')
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)

x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()

# animated=True tells matplotlib to only draw the artist when we
# explicitly request it
(ln,) = ax.plot(x, np.sin(x), animated=True)

plt.ylim([-20, 20])

# make sure the window is raised, but the script keeps going
plt.show(block=False)

# stop to admire our empty window axes and ensure it is rendered at
# least once.
#
# We need to fully draw the figure at its final size on the screen
# before we continue on so that :
#  a) we have the correctly sized and drawn background to grab
#  b) we have a cached renderer so that ``ax.draw_artist`` works
# so we spin the event loop to let the backend process any pending operations
plt.pause(0.1)

# get copy of entire figure (everything inside fig.bbox) sans animated artist
bg = fig.canvas.copy_from_bbox(fig.bbox)
# draw the animated artist, this uses a cached renderer
ax.draw_artist(ln)
# show the result to the screen, this pushes the updated RGBA buffer from the
# renderer to the GUI framework so you can see it
fig.canvas.blit(fig.bbox)



while True:
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    

        if data:
            ys = data.decode('ASCII').split(',')[2].strip()
            # reset the background back in the canvas state, screen unchanged
            fig.canvas.restore_region(bg)
            # update the artist, neither the canvas state nor the screen have changed
            ln.set_ydata(float(ys))
            # re-render the artist, updating the canvas state, but not the screen
            ax.draw_artist(ln)
            # copy the image to the GUI state, but screen might not be changed yet
            fig.canvas.blit(fig.bbox)
            # flush any pending GUI events, re-painting the screen if needed
            fig.canvas.flush_events()
    except socket.error as e:
        if e.args[0] == errno.EWOULDBLOCK: 
            print('no data')
            time.sleep(0.2)           # short delay, no tight loops
        else:
            print(e)
            break
    
    #print(data.decode('ASCII').split(',')[2])

