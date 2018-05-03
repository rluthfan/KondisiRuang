# import paho.mqtt.client as mqtt
import paho.mqtt.client as mqttClient
import time
import random, threading, json
from datetime import datetime

#====================================================
# MQTT Settings
''' 
MQTT_Broker = "192.168.0.132"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Humidity = "Home/BedRoom/DHT22/Humidity"
MQTT_Topic_Temperature = "Home/BedRoom/DHT22/Temperature"
#====================================================

def on_connect(client, userdata, flag, rc):
	if rc != 0:
		pass
		print ("Unable to connect to MQTT Broker...")
	else:
		print ("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		

mqttc = mqtt.Client()
mqttc.username_pw_set("rifqil", "rifqil")
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		
'''
# Setup MQTT begin
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

def on_publish(client, userdata, mid):
	pass

Connected = False   #global variable for the state of the connection
'''# Local Connection
broker_address= "192.168.0.116"      #Broker address
port = 1883                          #Broker port
user = "rifqil"                      #Connection username
password = "rifqil"                  #Connection password
'''
# RabbitMQ LSKK
broker_address= "167.205.7.226"            #Broker address
port = 1883                                #Broker port
user = "/kondisiruang:kondisiruang"        #Connection username
password = "kondisiruang"                  #Connection password

client = mqttClient.Client("Dummy_Sensor")         #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
#client.on_message= on_message                      #attach function to callback
client.on_publish= on_publish
 
client.connect(broker_address, port=port)          #connect to broker

def publish_To_Topic(topic, message):
	client.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print ("")
 
client.loop_start()        #start the loop
# client.loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)


while Connected != True:    #Wait for connection
    time.sleep(0.1)

toggle = 0
def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(1.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		message_dummy_data = {}
		message_dummy_data['MODE'] = "Normal"
		message_dummy_data['SENSOR_ID'] = 1
		message_dummy_data['TEMPERATURE'] = float("{0:.2f}".format(random.uniform(21,23)))
		message_dummy_data['HUMIDITY'] = float("{0:.2f}".format(random.uniform(50, 70)))
		message_dummy_data['LIGHT'] = random.randint(100, 300)
		message_dummy_data['SOUND'] = random.randint(30, 60)
		publish_To_Topic("kondisiruang/sensor", json.dumps(message_dummy_data))
		toggle = 1
	elif toggle == 1:
		message_dummy_data = {}
		message_dummy_data['MODE'] = "Normal"
		message_dummy_data['SENSOR_ID'] = 2
		message_dummy_data['TEMPERATURE'] = float("{0:.2f}".format(random.uniform(21,23)))
		message_dummy_data['HUMIDITY'] = float("{0:.2f}".format(random.uniform(50, 70)))
		message_dummy_data['LIGHT'] = random.randint(100, 300)
		message_dummy_data['SOUND'] = random.randint(30, 60)
		publish_To_Topic("kondisiruang/sensor", json.dumps(message_dummy_data))
		toggle = 2
	elif toggle == 2:
		message_dummy_data = {}
		message_dummy_data['MODE'] = "Normal"
		message_dummy_data['SENSOR_ID'] = 3
		message_dummy_data['TEMPERATURE'] = float("{0:.2f}".format(random.uniform(21,23)))
		message_dummy_data['HUMIDITY'] = float("{0:.2f}".format(random.uniform(50, 70)))
		message_dummy_data['LIGHT'] = random.randint(100, 300)
		message_dummy_data['SOUND'] = random.randint(30, 60)
		publish_To_Topic("kondisiruang/sensor", json.dumps(message_dummy_data))
		toggle = 3
	elif toggle == 3:
		message_dummy_data = {}
		message_dummy_data['MODE'] = "Normal"
		message_dummy_data['SENSOR_ID'] = 4
		message_dummy_data['TEMPERATURE'] = float("{0:.2f}".format(random.uniform(21,23)))
		message_dummy_data['HUMIDITY'] = float("{0:.2f}".format(random.uniform(50, 70)))
		message_dummy_data['LIGHT'] = random.randint(100, 300)
		message_dummy_data['SOUND'] = random.randint(30, 60)
		publish_To_Topic("kondisiruang/sensor", json.dumps(message_dummy_data))
		toggle = 0
publish_Fake_Sensor_Values_to_MQTT()  
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()
# Setup MQTT end

'''		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print ("")


#====================================================
# FAKE SENSOR 
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

toggle = 0

def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))

		Humidity_Data = {}
		Humidity_Data['Sensor_ID'] = "Dummy-1"
		Humidity_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		Humidity_Data['Humidity'] = Humidity_Fake_Value
		humidity_json_data = json.dumps(Humidity_Data)

		print ("Publishing fake Humidity Value: " + str(Humidity_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_Humidity, humidity_json_data)
		toggle = 1

	else:
		Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))

		Temperature_Data = {}
		Temperature_Data['Sensor_ID'] = "Dummy-2"
		Temperature_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		Temperature_Data['Temperature'] = Temperature_Fake_Value
		temperature_json_data = json.dumps(Temperature_Data)

		print ("Publishing fake Temperature Value: " + str(Temperature_Fake_Value) + "...")
		publish_To_Topic (MQTT_Topic_Temperature, temperature_json_data)
		toggle = 0


publish_Fake_Sensor_Values_to_MQTT()

#====================================================
'''
