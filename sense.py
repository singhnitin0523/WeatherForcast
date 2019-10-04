
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

sensor1 = BMP085.BMP085()


sensor = Adafruit_DHT.DHT11

#  DHT sensor
# connected to GPIO4.
pin = 4

def senseread():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    pressure=(sensor1.read_pressure())/100
    return temperature,humidity,pressure

x,y,z=senseread()