from PicoAirQuality import KitronikBME688, KitronikRTC, KitronikOLED, KitronikButton
import urequests as requests
import ujson
import network
import socket
import time


bme688 = KitronikBME688()
rtc = KitronikRTC()
buttons = KitronikButton()
oled = KitronikOLED()


bme688.setupGasSensor()
bme688.calcBaselines()


###################################################################################
########################### Mise à l'heure du module RTC ##########################


def setdate():
    rtc.setDate(3, 02, 2023)
    rtc.setTime(11 ,00, 00)
    rtc.setAlarm(11, 01, True, 1, 0)


###################################################################################
########################### Envoi des données à l'API #############################


def sendDatas():
    
    bme688.measureData()
    
    temp = str(bme688.readTemperature())
    press = str(bme688.readPressure())
    hum = str(bme688.readHumidity())
    IAQ = str(bme688.getAirQualityScore())
    CO2 = str(bme688.readeCO2())
    
    datas = {'temp':temp,
            'press':press,
            'hum':hum,
            'IAQ':IAQ,
            'CO2':CO2}
    
    header = ''
    url = 'http://10.0.0.14:5000/addRambouillet'
    r = requests.post(url, json = datas)
    response = r.text
    
    print(response)
    
    
####################################################################################
########################### Connection à la box ####################################


def connect():
    #Connect to WLAN
    
    ssid = 'NETGEAR00'
    password = 'Anapurna01'
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print('Connected on: ' + ip)
    return True


#####################################################################################
######################### Affichage temps réel des données ##########################


def affichage():
    bme688.measureData()
    oled.displayText("Temp: " + str(bme688.readTemperature()) + " C", 1)
    oled.displayText("Pres: " + str(bme688.readPressure()) + " Pa", 2)
    oled.displayText("Hum: " + str(bme688.readHumidity()) + " %", 3)
    oled.displayText("IAQ: " + str(bme688.getAirQualityScore()), 4)
    oled.displayText("eCO2: " + str(bme688.readeCO2()) + " ppm", 5)
    oled.show()
    oled.clear()
    

#####################################################################################
########################### Boucle du programme #####################################

setdate()
while(1):
    #affichage des données météo par appui sur le bouton A
    if (buttons.buttonA.value() == True):
        affichage()
        oled.clear()
    
    #envoi des données manuel
    if (buttons.buttonB.value() == True):
        oled.clearLine(3)
        oled.displayText("sending to API", 3)
        oled.show()
        time.sleep(2)
        try:
            connection = connect()
            print('connection')
        except KeyboardInterrupt:
            machine.reset()
            
        if connection:
            sendDatas()
        
        rtc.silenceAlarm()
        oled.clearLine(3)
        oled.show()
        
    #envoi des données automatique
    if(rtc.checkAlarm()):
        oled.clearLine(3)
        oled.displayText("sending to API", 3)
        oled.show()
        time.sleep(2)
        try:
            connection = connect()
        except KeyboardInterrupt:
            machine.reset()
            
        if connection:
            sendDatas()
        
        rtc.silenceAlarm()
        oled.clearLine(3)
        oled.show()
        
        
