# Libraries
import paho.mqtt.client as mqttClient
import time
import sys, os, json, pika
import MySQLdb
from datetime import datetime

# Setup Database begin
# Open Database Connection
db = MySQLdb.connect("localhost", "root", "password", "kelas1")

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

'''
# Kalo pake RabbitMQ local
# Setup AMQP begin
credentials = pika.PlainCredentials('rifqil', 'rifqil')
# IP Address-nya diganti jangan lupa
parameters = pika.ConnectionParameters('192.168.0.116',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection()
#pika.ConnectionParameters(host='192.168.0.132'))
'''

# Setup AMQP begin
credentials = pika.PlainCredentials('kondisiruang', 'kondisiruang')
parameters = pika.ConnectionParameters('167.205.7.226',
                                       5672,
                                       '/kondisiruang',
                                       credentials)

connection = pika.BlockingConnection(parameters)
#pika.ConnectionParameters(host='192.168.0.132'))

channel = connection.channel()

channel.queue_declare(queue='holosensor',
                        durable=True)

channel.exchange_declare(exchange='amq.topic',
                        exchange_type='topic',
                            durable=True
                            )
# Setup AMQP end

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
    # Date_and_Time = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
    Daten = (datetime.today()).strftime("%Y-%m-%d")
##    Daten = (datetime.today()).strftime("%Y-%m-01")
    Timen = (datetime.today()).strftime("%H:%M:%S.%f")
##    Timen = (datetime.today()).strftime("11:%M:%S.%f")
    Mode_Pembelajaran = json_Dict['MODE']
    SensorID = json_Dict['SENSOR_ID']
    tempdata = json_Dict['TEMPERATURE']
    humidata = json_Dict['HUMIDITY']
    lightdata = json_Dict['LIGHT']
    sounddata = json_Dict['SOUND']

    # Habis ini harus coba print dulu yang angka-angka (sensorID ke bawah) di konsol

    # Prototype
    # Creating Recommendation
    
    # Mode Pembelajaran Diskusi
    if (Mode_Pembelajaran == "Diskusi"):
        # Recommendation Temperature
        if (tempdata > 27.0):
            recomtempdata = "Suhu terlalu tinggi, buka ventilasi"
        elif ((tempdata >= 23.0) and (tempdata <= 27.0)):
            recomtempdata = "No Recommendation"
        elif (tempdata < 23.0):
            recomtempdata = "Suhu cukup rendah, tutup ventilasi"

        # Recommendation Humidity
        if (humidata > 80.0):
            recomhumiddata = "Tutup Jendela"
        elif ((humidata >= 30.0) and (humidata <= 80.0)):
            recomhumiddata = "No Recommendation"
        elif (humidata < 30.0):
            recomhumiddata = "Humidity too Low"

        # Recommendation Light
        if (lightdata > 5000):
            recomlightdata = "Tutup Jendela"
        elif (lightdata > 500) and (lightdata <= 5000):
            recomlightdata = "Matikan Lampu"
        elif (lightdata >= 300) and (lightdata <= 500):
            recomlightdata = "No Recommendation"
        elif (lightdata < 300):
            recomlightdata = "Nyalakan Lampu"

        # Recommendation Sound
        if (sounddata > 45):
            recomsounddata = "Ruangan terlalu berisik"
        elif ((sounddata >= 20) and (sounddata <= 45)):
            recomsounddata = "No Recommendation"

    # Mode Pembelajaran Presentasi
    elif (Mode_Pembelajaran == "Presentasi"):
        # Recommendation Temperature
        if (tempdata > 27.0):
            recomtempdata = "Suhu terlalu tinggi, buka ventilasi"
        elif ((tempdata >= 23.0) and (tempdata <= 27.0)):
            recomtempdata = "No Recommendation"
        elif (tempdata < 23.0):
            recomtempdata = "Suhu cukup rendah, tutup ventilasi"

        # Recommendation Humidity
        if (humidata > 80.0):
            recomhumiddata = "Tutup Jendela"
        elif ((humidata >= 30.0) and (humidata <= 80.0)):
            recomhumiddata = "No Recommendation"
        elif (humidata < 30.0):
            recomhumiddata = "Humidity too Low"

        # Recommendation Light
        if (lightdata > 5000):
            recomlightdata = "Tutup Jendela"
        elif (lightdata > 500) and (lightdata <= 5000):
            recomlightdata = "Matikan Lampu"
        elif (lightdata >= 300) and (lightdata <= 500):
            recomlightdata = "No Recommendation"
        elif (lightdata < 300):
            recomlightdata = "Nyalakan Lampu"

        # Recommendation Sound
        if (sounddata > 45):
            recomsounddata = "Ruangan terlalu berisik"
        elif ((sounddata >= 20) and (sounddata <= 45)):
            recomsounddata = "No Recommendation"
    
    # Mode Pembelajaran Normal
    else:
        # Recommendation Temperature
        if (tempdata > 27.0):
            recomtempdata = "Suhu terlalu tinggi, buka ventilasi"
        elif ((tempdata >= 23.0) and (tempdata <= 27.0)):
            recomtempdata = "No Recommendation"
        elif (tempdata < 23.0):
            recomtempdata = "Suhu cukup rendah, tutup ventilasi"

        # Recommendation Humidity
        if (humidata > 80.0):
            recomhumiddata = "Tutup Jendela"
        elif ((humidata >= 30.0) and (humidata <= 80.0)):
            recomhumiddata = "No Recommendation"
        elif (humidata < 30.0):
            recomhumiddata = "Humidity too Low"

        # Recommendation Light
        if (lightdata > 5000):
            recomlightdata = "Tutup Jendela"
        elif (lightdata > 500) and (lightdata <= 5000):
            recomlightdata = "Matikan Lampu"
        elif (lightdata >= 300) and (lightdata <= 500):
            recomlightdata = "No Recommendation"
        elif (lightdata < 300):
            recomlightdata = "Nyalakan Lampu"

        # Recommendation Sound
        if (sounddata > 45):
            recomsounddata = "Ruangan terlalu berisik"
        elif ((sounddata >= 20) and (sounddata <= 45)):
            recomsounddata = "No Recommendation"
        else:
            recomsounddata = "Tidak Mungkin Terjadi"


    # # Prepare SQL query to INSERT a record into the database.
    # sql = "INSERT INTO holosensor1(date_n_time, sensor_id, temperature, recommend_temperature, humidity, recommend_humidity, light_intensity, recommend_light, sound_intensity, recommend_sound) \
    #        VALUES ('%s', '%d', '%lf', '%s', '%lf', '%s', '%d', '%s', '%d', '%s')" % \
    #        (Date_and_Time, SensorID, tempdata, recomtempdata, humidata, recomhumiddata, lightdata, recomlightdata, sounddata, recomsounddata)
    # # Process Input Data to database Holosensor
    # eksekusi (sql, "Input database Berhasil", "GAGAL")

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO sensors_datum(date_n, time_n, mode_belajar, sensor_id, temperature, recommend_temperature, humidity, recommend_humidity, light_intensity, recommend_light, sound_intensity, recommend_sound) \
           VALUES ('%s', '%s', '%s', '%d', '%lf', '%s', '%lf', '%s', '%d', '%s', '%d', '%s')" % \
           (Daten, Timen, Mode_Pembelajaran, SensorID, tempdata, recomtempdata, humidata, recomhumiddata, lightdata, recomlightdata, sounddata, recomsounddata)
    # Process Input Data to database Holosensor
    eksekusi (sql, "Input database Berhasil", "GAGAL")

    # Initializing sensor data to be sent
    msgJson={}
    # msgJson["DATE_AND_TIME"] = Date_and_Time
    msgJson["DATE"] = Daten
    msgJson["TIME"] = Timen
    msgJson["SENSOR_ID"] = SensorID
    msgJson["TEMPERATURE"] = tempdata
    msgJson["RECOMTEMP"] = recomtempdata
    msgJson["HUMIDITY"] = humidata
    msgJson["RECOMHUMID"] = recomhumiddata
    msgJson["LIGHTINTENSITY"] = lightdata
    msgJson["RECOMLIGHT"] = recomlightdata
    msgJson["SOUNDLEVEL"] = sounddata
    msgJson["RECOMSOUND"] = recomsounddata
    
    # properties = pika.BasicProperties(content_type = "application/json", delivery_mode = 1)

    # Sending sensor data with recommendation
    channel.basic_publish(exchange='amq.topic', routing_key='holosensor.data', body= json.dumps(msgJson))
 
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
 
client = mqttClient.Client("Raspi")                #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
# client.loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("kondisiruang/sensor")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
    connection.close()
# Setup MQTT end
