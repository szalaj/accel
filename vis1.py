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

x = [0]
 
T = [a[0] for a in rows]

tit = []

for i in range(1,len(T)):
    tprev = T[i-1]
    ti = T[i]
    dt = (ti - tprev).total_seconds()
    tit.append(dt)

print(sum(tit))

ax = [a[1] for a in rows]
ay = [a[2] for a in rows]
az = [a[3] for a in rows]
plt.plot(T, ax)
plt.plot(T, ay)
plt.plot(T, az)
plt.show()