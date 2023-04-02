from PicoAirQuality import KitronikBME688, KitronikRTC, KitronikOLED
import urequests as requests
import ujson
import network
import socket


bme688 = KitronikBME688()
rtc = KitronikRTC()
buttons = KitronikButton()


bme688.setupGasSensor()
bme688.calcBaselines()



ssid = 'NETGEAR00'
password = 'Anapurna01'


###################################################################################
########################### Mise à l'heure du module RTC ##########################


def setdate():
    rtc.setDate(2, 02, 2023)
    rtc.setTime(10 ,18, 00)
    rtc.setAlarm(14, 2, True, 1, 0)


###################################################################################
########################### Envoi des données à l'API #############################


def sendDatas():
    
    bme688.measureData()
    
    temp = bme688.readTemperature()
    press = bme688.readPressure()
    hum = bme688.readHumidity()
    IAQ = bme688.getAirQualityScore()
    CO2 = bme688.readeCO2()
    
    datas = ujson.dump{'temp':temp,
                       'press':press,
                       'hum':hum,
                       'IAQ':IAQ,
                       'CO2':CO2}
    
    headers = {'Accept': 'application/json'}
    
    r = requests.post('http://10.0.0.14:5000/addRambouillet', headers = headers, data)
    response = r.json
    
    return response
    
    
####################################################################################
########################### Connection à la box ####################################


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print('Connected on: ' + ip)
    return True


#####################################################################################
######################### Affichage temps réel des données ##########################


def affichage():
    bme688.measureData()
    oled.clear()
    oled.displayText("Temp: " + str(bme688.readTemperature()) + " C", 1)
    oled.displayText("Pres: " + str(bme688.readPressure()) + " Pa", 2)
    oled.displayText("Hum: " + str(bme688.readHumidity()) + " %", 3)
    oled.displayText("IAQ: " + str(bme688.getAirQualityScore()), 4)
    oled.displayText("eCO2: " + str(bme688.readeCO2()) + " ppm", 5)
    oled.show()
    sleep_ms(5000)
    

#####################################################################################
########################### Boucle du programme #####################################


while(1):
    #affichage des données météo par appui sur le bouton A
    if (buttons.buttonA.value() == True):
        affichage()
    
    #envoi des données automatique ou manuel
    if (rtc.checkAlarm() or buttons.buttonB.value() == True):
        oled.clearLine(3)
        oled.displayText("sending to API")
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
        
    if():
        
        
        
            
        
        

