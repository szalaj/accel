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