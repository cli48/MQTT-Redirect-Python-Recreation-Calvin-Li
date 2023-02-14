import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker ="mqtt.things.ph"
client = mqtt.Client(client_id="Re-direction broker Calvin", clean_session=False) #gives client a name
client.username_pw_set("63e964c00317e3273ecc3165","PQ6xg1TCIKTuSf0QgpFER7c3") #password and user authentication
client.connect(mqttBroker) #connects to broker

while True:
    randNumber = uniform(20.0,21.0) #generates random numbers
    client.publish("Random_Nums",randNumber,qos=0,retain=False)
    print("Just published " + str(randNumber)+ "to topic Random_Nums")
    time.sleep(1)