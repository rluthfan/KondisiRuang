# Libraries
import paho.mqtt.client as mqttClient
import time
import sys, os, json, pika
import MySQLdb
from datetime import datetime

# Setup Database begin
# Open Database Connection
db = MySQLdb.connect("192.168.0.103", "adminsql", "adminsql", "kelas1")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute table function
def eksekusi(sql, done, err):
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        if done != " ":
            print done
    except:
        # Rollback in case there is any error
        db.rollback()
        if err != " ":
            print err
#Setup Database end

# Setup MQTT begin
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print "Message Received: "  + message.payload
    
    # Parsing JSON data
    json_Dict = json.loads(message.payload)
    Daten = (datetime.today()).strftime("%Y-%m-%d")
    Timen = (datetime.today()).strftime("%H:%M:%S.%f")

    Mode_Pembelajaran = json_Dict['MODE']
    SensorID = json_Dict['SENSOR_ID']
    tempdata = json_Dict['TEMPERATURE']
    humidata = json_Dict['HUMIDITY']
    lightdata = json_Dict['LIGHT']
    sounddata = json_Dict['SOUND']

    # Prototype
    # Creating Recommendation

    # Recommendation Temperature
    if (tempdata >= 31.0):
        recomtempdata = "Di Atas Ambang Batas, Buka Ventilasi!, Nyalakan aktuator!"
    elif ((tempdata >= 28.0) and (tempdata < 31.0)):
        recomtempdata = "Mendekati Ambang Batas, Saran: Buka Ventilasi"
    elif ((tempdata >= 25.8) and (tempdata < 28.0)):
        recomtempdata = "Hangat Nyaman"
    elif ((tempdata >= 22.8) and (tempdata < 25.8)):
        recomtempdata = "Nyaman Optimal"
    elif ((tempdata >= 20.5) and (tempdata < 22.8)):
        recomtempdata = "Sejuk Nyaman, Matikan Aktuator!, Saran: Tutup Ventilasi"
    elif (tempdata < 20.5):
        recomtempdata = "Di Bawah Sejuk Nyaman, Tutup Ventilasi!"

    # Recommendation Humidity
    if (humidata > 80.0):
        recomhumiddata = "Di Atas Ambang Batas Kelembapan"
    elif ((humidata > 70.0) and (humidata <= 80.0)):
        recomhumiddata = "Lembap Nyaman"
    elif ((humidata > 60.0) and (humidata <= 70.0)):
        recomhumiddata = "Nyaman Optimal"
    elif ((humidata > 50.0) and (humidata <= 60.0)):
        recomhumiddata = "Kering Nyaman"
    elif (humidata <= 50.0):
        recomhumiddata = "Di Bawah Kering Nyaman"

    # Recommendation Light
    if(Mode_Pembelajaran == "Presentasi"):
        if (lightdata > 1000):
            recomlightdata = "Terlalu Terang, Matikan Lampu!, Tutup Jendela!"
        elif (lightdata > 700) and (lightdata <= 1000):
            recomlightdata = "Cukup Terang, Matikan Lampu!"
        elif (lightdata > 500) and (lightdata <= 700):
            recomlightdata = "Terang Nyaman"
        elif (lightdata >= 300) and (lightdata <= 500):
            recomlightdata = "Nyaman Optimal"
        elif (lightdata > 250) and (lightdata < 300):
            recomlightdata = "Redup Nyaman, Saran: Nyalakan Lampu"
        elif (lightdata <= 250):
            recomlightdata = "Terlalu Redup, Nyalakan Lampu!"
    else:
        if (lightdata > 250):
            recomlightdata = "Terlalu Terang, Matikan Lampu!, Tutup Jendela!"
        elif (lightdata > 150) and (lightdata <= 250):
            recomlightdata = "Mendekati Ambang Batas, Matikan Lampu!"
        elif (lightdata > 100) and (lightdata <= 150):
            recomlightdata = "Terang Nyaman"
        elif (lightdata >= 50) and (lightdata <= 100):
            recomlightdata = "Nyaman Optimal"
        elif (lightdata > 10) and (lightdata < 50):
            recomlightdata = "Redup Nyaman"
        elif (lightdata <= 10):
            recomlightdata = "Terlalu Redup, Nyalakan Lampu Kecil!"

    # Recommendation Sound
    if(Mode_Pembelajaran == "Normal"):
        if (sounddata > 60):
            recomsounddata = "Di Atas Ambang Batas Kebisingan!"
        elif ((sounddata > 50) and (sounddata <= 60)):
            recomsounddata = "Mulai Bising, Mendekati Ambang Batas"
        elif ((sounddata > 40) and (sounddata <= 50)):
            recomsounddata = "Nyaman Optimal"
        elif (sounddata <= 40):
            recomsounddata = "No Recommendation"
    # Mode Pembelajaran Presentasi
    elif(Mode_Pembelajaran == "Presentasi"):
        if (sounddata > 60):
            recomsounddata = "Di Atas Ambang Batas Kebisingan!"
        elif ((sounddata > 55) and (sounddata <= 60)):
            recomsounddata = "Mulai Bising, Mendekati Ambang Batas"
        elif ((sounddata > 50) and (sounddata <= 55)):
            recomsounddata = "Nyaman Optimal"
        elif (sounddata <= 50):
            recomsounddata = "No Recommendation"
    elif(Mode_Pembelajaran == "Diskusi"):
        if (sounddata > 70):
            recomsounddata = "Di Atas Ambang Batas Kebisingan!"
        elif ((sounddata > 65) and (sounddata <= 70)):
            recomsounddata = "Mulai Bising, Mendekati Ambang Batas"
        elif ((sounddata > 60) and (sounddata <= 65)):
            recomsounddata = "Nyaman Optimal"
        elif (sounddata <= 60):
            recomsounddata = "No Recommendation"

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO sensors_datum(date_n, time_n, mode_belajar, sensor_id, temperature, recommend_temperature, humidity, recommend_humidity, light_intensity, recommend_light, sound_intensity, recommend_sound) \
           VALUES ('%s', '%s', '%s', '%d', '%lf', '%s', '%lf', '%s', '%d', '%s', '%d', '%s')" % \
           (Daten, Timen, Mode_Pembelajaran, SensorID, tempdata, recomtempdata, humidata, recomhumiddata, lightdata, recomlightdata, sounddata, recomsounddata)
    # Process Input Data to database Holosensor
    eksekusi (sql, "Input database Berhasil", "GAGAL")

Connected = False   #global variable for the state of the connection

'''
# Kalo connect ke RabbitMQ Local
# Jangan lupa ganti IP Address
broker_address= "192.168.0.116"      #Broker address
port = 1883                          #Broker port
user = "rifqil"                      #Connection username
password = "rifqil"                  #Connection password
'''
 
broker_address= "167.205.7.226"            #Broker address
port = 1883                                #Broker port
user = "/kondisiruang:kondisiruang"        #Connection username
password = "kondisiruang"                  #Connection password
 
client = mqttClient.Client("PC-DBServer")          #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
# client.loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("kondisiruang/dataserver")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
# Setup MQTT end
