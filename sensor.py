
# ? IMPORTAR LIBRERÍAS NECESARIASimport network
import network
import urequests
import time
import random
from dht import DHT11
from machine import Pin as pin

# ? INSTANCIA SENSOR DE AMBIENTE
sensor = DHT11(pin(15))

# ? CONEXIÓN A LA RED
def wifi(red, password):
    global miRed
    miRed = network.WLAN(network.STA_IF)

    if not miRed.isconnected():
        miRed.active(True)
        miRed.connect(red, password)
        print('Conectando a la red', red + "...")
        timeout = time.time()
        while not miRed.isconnected():
            if (time.ticks_diff(time.time(), timeout) > 10):
                return False
    return True

if wifi("Q60", "minumero"):
    print("¡Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    url = "https://api.thingspeak.com/update?api_key=N7L1OOYI6Y4IKQDL"

# ? CICLO PRINCIPAL
    while True:
        time.sleep(0.3)
        sensor.measure()
        temperatura = sensor.temperature()
        humedad = sensor.humidity()
        presion = random.randint(559, 563)
        # print("T={:02d}°C, H={:02d}%, P={:02d}Torr".format(
        #     temperatura, humedad, presion))
        # ~ ENVÍA LOS DATOS A THING-SPEAK
        respuesta = urequests.get(
            url+"&field1="+str(temperatura)+"&field2="+str(humedad)+"&field3="+str(presion))
        # print(respuesta.text)
        # print(respuesta.status_code)
        respuesta.close()

else:
    print("No se pudo conectar")
    miRed.active(False)
