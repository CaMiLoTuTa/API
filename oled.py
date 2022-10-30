
# ? IMPORTAR LIBRERÍAS NECESARIAS
import network
import time
import urequests
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# ? INSTANCIA PANTALLA OLED
i2c = I2C(0, scl=Pin(27), sda=Pin(14))
ancho, alto = 128, 64
oled = SSD1306_I2C(ancho, alto, i2c)

# ? INSTANCIA BOTONES
botonRojo = Pin(32, Pin.IN, Pin.PULL_UP)
botonNegro = Pin(33, Pin.IN, Pin.PULL_UP)
botonBlanco = Pin(26, Pin.IN, Pin.PULL_UP)

#? URLS PARA ENVIAR INFORMACIÓN Y RECIBIR
url = "https://maker.ifttt.com/trigger/notamb/with/key/inSrLr4nyMQ8ShQ0noTQEo4Hy2fO1f4ZYMVvxUEUW13"
urlDis = "https://maker.ifttt.com/trigger/ambnot/with/key/inSrLr4nyMQ8ShQ0noTQEo4Hy2fO1f4ZYMVvxUEUW13?"
urlSMS = "https://maker.ifttt.com/trigger/sms/with/key/inSrLr4nyMQ8ShQ0noTQEo4Hy2fO1f4ZYMVvxUEUW13?"
urlTel = "https://maker.ifttt.com/trigger/telegram_not/with/key/inSrLr4nyMQ8ShQ0noTQEo4Hy2fO1f4ZYMVvxUEUW13?"

# ? CONEXIÓN A LA RED
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Q60", "minumero")

# ? PANTALLA DE ESPERA MIENTRAS CONECTA
while not sta_if.isconnected():
    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text(" CONNECTING.", 0, 30)
    oled.text("*"*16, 0, 57)
    oled.show()
    time.sleep(0.5)

    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text(" CONNECTING..", 0, 30)
    oled.text("*"*16, 0, 57)
    oled.show()
    time.sleep(0.5)

    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text(" CONNECTING...", 0, 30)
    oled.text("*"*16, 0, 57)
    oled.show()
    time.sleep(0.5)

# ? PANTALLA CUANDO ESTE CONECTADO A LA RED
oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   CONNECTED", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.15)

oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   ", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.15)

oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   CONNECTED", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.15)

oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   ", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.15)

oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   CONNECTED", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.15)

oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   ", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.15)

oled.fill(0)
oled.text("*"*16, 0, 0)
oled.text("   CONNECTED", 0, 30)
oled.text("*"*16, 0, 55)
oled.show()
time.sleep(0.5)

# ? PANTALLA PRINCIPAL
def presionar():
    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text("     BOTON", 0, 10)
    oled.text("Rojo-Temperatura", 0, 22)
    oled.text("Negro-Humedad", 0, 34)
    oled.text("Blanco-Presion", 0, 46)
    oled.text("*"*16, 0, 57)
    oled.show()
    time.sleep(2)

# ? DEPENDE DEL BOTON PRESIONADO MOSTRARA LA INFORMACIÓN
def temperaturaOled():
    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text("TEMPERATURA: "+str(temperatura)+"C", 0, 30)
    oled.text("*"*16, 0, 57)
    oled.show()

def humedadOled():
    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text("HUMEDAD: "+str(humedad)+"%", 0, 30)
    oled.text("*"*16, 0, 57)
    oled.show()

def presionOled():
    oled.fill(0)
    oled.text("*"*16, 0, 0)
    oled.text("PRESION: "+str(presion)+"Torr", 0, 30)
    oled.text("*"*16, 0, 57)
    oled.show()

# ? ENVÍA LOS DATOS RECIBIDOS A LOS SERVICIOS DE IFTTT Y A LA PANTALLA OLED
def enviarMensaje():
    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        presionar()
    respuestaDis = urequests.get(
        urlDis+"&value1="+str(temperatura) + "&value2="+str(humedad)+"&value3="+str(presion))
    respuestaDis.close()
    if botonRojo.value() == 0 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        temperaturaOled()
    if botonRojo.value() == 1 and botonNegro.value() == 0 and botonBlanco.value() == 1:
        humedadOled()
    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 0:
        presionOled()

    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        presionar()
    respuestaSMS = urequests.get(
        urlSMS+"&value1="+str(temperatura) + "&value2="+str(humedad)+"&value3="+str(presion))
    respuestaSMS.close()
    if botonRojo.value() == 0 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        temperaturaOled()
    if botonRojo.value() == 1 and botonNegro.value() == 0 and botonBlanco.value() == 1:
        humedadOled()
    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 0:
        presionOled()

    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        presionar()
    respuestaTel = urequests.get(
        urlTel+"&value1="+str(temperatura) + "&value2="+str(humedad)+"&value3="+str(presion))
    respuestaTel.close()
    if botonRojo.value() == 0 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        temperaturaOled()
    if botonRojo.value() == 1 and botonNegro.value() == 0 and botonBlanco.value() == 1:
        humedadOled()
    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 0:
        presionOled()


# ? CICLO PRINCIPAL
while True:
    # ~ VERIFICA EL VALOR DE LOS BOTONES Y MOSTRARA EL VALOR A PEDIR 
    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        presionar()
    # ~ RECIBE LOS DATOS 
    consulta = urequests.get(
        "https://api.thingspeak.com/channels/1909834/feeds.json?results=2")
    datos = consulta.json()
    # ~ VARIABLES DONDE SE GUARDARAN LOS DATOS DEL ARCHIVO JSON
    temperatura = datos["feeds"][1]["field1"]
    humedad = datos["feeds"][1]["field2"]
    presion = datos["feeds"][1]["field3"]

    # ~ VERIFICA EL VALOR DE LOS BOTONES Y MOSTRARA EL VALOR A PEDIR 
    if botonRojo.value() == 0 and botonNegro.value() == 1 and botonBlanco.value() == 1:
        temperaturaOled()
    if botonRojo.value() == 1 and botonNegro.value() == 0 and botonBlanco.value() == 1:
        humedadOled()
    if botonRojo.value() == 1 and botonNegro.value() == 1 and botonBlanco.value() == 0:
        presionOled()

    enviarMensaje()
