import matplotlib.pyplot as plt
import numpy as np
import datetime
import psycopg2


conn = psycopg2.connect(dbname="postgres", user="postgres", password="Robak123", host="localhost", port=5432)

cur = conn.cursor()

cur.execute("SELECT * FROM accel")

rows = cur.fetchall()

print(len(rows))
        


cur.close()
conn.close()

t = [a[0] for a in rows]
ax = [a[1] for a in rows]
ay = [a[2] for a in rows]
az = [a[3] for a in rows]
plt.plot(t, ax)
plt.plot(t, ay)
plt.plot(t, az)
plt.show()