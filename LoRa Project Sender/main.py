import time
from lora import LoRa
from time import sleep


#se inicializa el objeto de lora sin header
lora = LoRa()

#en el caso de que se desee un header para el filtrado de los mensajes
#lorawhead = LoRa(header = 'header')
#de manera los mensajes llevaran ese header para ser filtrados de otros

#send(msg) envia msg a traves del chip de lora
msg = 'hola desde tierra'
print('hola desde tierra')

counter = 0
print("LoRa Sender")

while True:
    payload = 'Hello ({0})'.format(counter)
    print("Sending packet: \n{}\n".format(payload))

    lora.send(payload)

    counter += 1
    time.sleep(1)