import Adafruit_DHT
import sqlite3
import requests
import time
conn=sqlite3.connect("dht11.db")
c = conn.cursor() ;
sensor = Adafruit_DHT.DHT11
pin = 4
humidity,temperature = Adafruit_DHT.read_retry(sensor, pin)

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tempeh(temperature1 numeric , humidity1 numeric)')
             
if humidity is not None and temperature is not None:
    a = temperature
    b = humidity
    print (str(a))
    print (str(b))
   
    create_table()
   
    c.execute(" INSERT INTO tempeh (temperature1,humidity1) values(?,?)", (a,b))
    c.execute(' SELECT * FROM tempeh')
    conn.commit()
   
    for row in c :
        a = row[0]
        b = row[1]
        print (str(a) +  "   " + str(b))
        queries = {"api_key": "07G0K4CHDRLD2N9R",
               "field1": a,
               "field2": b
                 }
        r = requests.get('https://api.thingspeak.com/update', params=queries)
else :
    print (' fail ')