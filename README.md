# Micropython_SX1278_LoRa
Proyecto para enviar y recibir datos a través de una placa ESP32 y el modulo SX1278 LoRa gestionado con Micropython.

---
__ESP32 Pages :)__

- __[SX1278 LoRa Module](https://wei1234c.blogspot.com/2017/08/sx127x-lora-transceiver-driver-for.html)__ - Información base para el uso del modulo SX127x LoRa en conjunto con la placa ESP32, gestionado con Micropython.


---

## LoRa SX1278 (Modulo de comunicación LoRa)   8-)

El repositorio consta de dos carpetas:
- LoRa Project Receiver (contenido para recibir paquetes)
- LoRa Project Sender (contenido para enviar paquetes)
---

La idea es desplegar el contenido de cada carpeta en placas ESP32 diferentes y ejecutarlas, al poco tiempo observaras como empiezan a llegar los paquetes (mostrandose en la terminal).
Teniendo esto como base, se pueden modificar cada fichero para afinar el funcionamiento a lo deseado.

**A continuación como deben ser las conexiones del modulo LoRa y la placa ESP32**

### ESP32 vs LoRa SX127x

| Puerto ESP32 | Pin en el Modulo LoRa |
| ------------ | ---------------- |
| 3.3V   | Positivo (3V3) |
| GND    | Puerto tierra (GND)  |
| P26    | Puerto DIO0 |
| P27    | Puerto MOSI |
| P14    | Puerto RST |
| P19    | Puerto MISO |
| P18    | Puerto NSS |
| P5     | Puerto SCK |

## Images

![ESP32 Placa](https://github.com/Maxss5/Micropython_BME680_-_Oled/blob/develop/images/ESP32Board.png "Placa ESP32")
![SSD1306 Oled Funcionando](https://github.com/Maxss5/Micropython_BME680_-_Oled/blob/develop/images/ssd1306_OLED.png "Oled SSD1306")
![bme680 Sensor](https://github.com/Maxss5/Micropython_BME680_-_Oled/blob/develop/images/bme680Sensor.png "Sensor BME6806")