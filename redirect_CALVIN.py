import paho.mqtt.client as mqtt
import time
#vars--------------------------------------------------------------------------------------------------------------
ClientID_Calvin = "Re_direct_broker_MQTT_CALVIN"
broker="mqtt.things.ph" #Can use IP or DNS of your broker, MQTT LENS IS NOT THE BROKER.

#end of vars-------------------------------------------------------------------------------------------------------

#defs
def on_connect(client, userdata, flags, rc): #function lets me know if connection is established else gives return code
   if rc==0:
        print("Connection ok.\n")
   else:
        print("Bad connection. Return code = ",rc)


#end of defs--------------------------------------------------------------------------------------------------------------

mqtt.Client(client_id="Test", clean_session=False)
#client_id refers to Client ID on MQTTlens, clean session determines if broker info is wiped
#userdata = Payload being sent,protocal is version of MQTT, either  MQTTv31 or MQTTv311 (web sockets), transport is declaring the usage of TCP protocal

client = mqtt.Client(ClientID_Calvin) #Client ID name, dont confuse for connection name. Variable up top for ease of use.
client.on_connect = on_connect #on_connect callback function to determine when MQTT client connects successfully w/o blocking the execution of the rest of the program.

print("Connecting to broker: ",broker)

client.connect(broker)

time.sleep(4) #allows 4 seconds of time to pass so connection can be established before continuing
client.loop_start()


client.loop_stop()
client.disconnect()





