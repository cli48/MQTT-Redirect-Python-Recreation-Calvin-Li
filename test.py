import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from random import randrange, uniform
import time
import json

def on_message(client, obj, msg): #handling of code from subscribed topics
    #print(msg.payload.decode())
    payload_string = msg.payload.decode()
    #print(payload_string)
    data = json.loads(payload_string) #unpackages and offloads data from JSON into an accessible list

    temp = data['payload_fields']['temperature'] #extracting values into workable numbers
    pressure = data['payload_fields']['pressure']
    altitude = data['payload_fields']['altitude']

    temp = (temp*1.8) + 32 #convert C to F
    pressure = pressure/6.895 #convert kpa to psi
    altitude = altitude*3.281 #Meters to feet

    edited_sensor_data = {"hardware_serial": "ESP_32", #Re serializes JSON into a string format for publishing
               "payload_fields": {"temperature": temp,
                                  "pressure": pressure,
                                  "altitude": altitude}}
    #print(payload_string)
    print(edited_sensor_data)

    client.publish("test2",edited_sensor_data,qos=0,retain=False) #publish edited data to topic "test2"
    print("Published\n")
    #time.sleep(1)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("Testing")


mqttBroker ="mqtt.things.ph"
client = mqtt.Client(client_id="Re-direction_broker_MQTT_CALVIN", clean_session=False) #gives client a name
client.username_pw_set("63e964c00317e3273ecc3165","PQ6xg1TCIKTuSf0QgpFER7c3") #password and user authentication
client.connect(mqttBroker) #connects to broker
client.on_message = on_message
client.on_connect = on_connect


client.loop_forever()



# while True: #code is for testing the publishing feature
#     randNumber = uniform(20.0,21.0) #generates random numbers
    
#     client.publish("Random_Nums",randNumber,qos=0,retain=False)
#     print("Just published " + str(randNumber)+ "to topic Random_Nums")
#     time.sleep(1)

