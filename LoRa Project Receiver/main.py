from lora import LoRa
import time

#se inicializa el objeto de lora sin header
lora = LoRa()

global_var = 0

#en el caso de que se desee un header para el filtrado de los mensajes
#lorawhead = LoRa(header = 'header')
#de manera que asi solo los mensajes que tengan esa cabecera seran recibidos

#funcion de callback necesaria para manejar mensajes de entrada
def toPrintMssg(msg):
    print("He recibido el siguiente mensaje ")
    print(msg)

lora.set_callback(toPrintMssg) #se especifica que funcion funcionara de callback
#lora.wait_msg() #se dispone a escuchar mensajes entrantes en segundo plano

#para el recibimiento de un mensaje en un momento especifico usar
while True:
    print("Recibiendo: ")
    #lora.wait_msg()
    lora.receive_msg()
    
    time.sleep(5)