import paho.mqtt.client as mqtt

ClientID_Calvin = "Re_direct_broker_MQTT_CALVIN"
def on_connect(client, userdata, flags, rc): #function lets me know if connection is established
   if rc==0:
      print("connected! Nice.\n")

client = mqtt.Client(ClientID_Calvin) #Client ID name, dont confuse for connection name. Variable up top for ease of use.

broker_address="mqtt.things.ph" #Can use IP or DNS to resolve IP address to connect to broker

Client(client_id="Test", clean_session=False, userdata=None, protocol=MQTTv311, transport="tcp")
#client_id refers to Client ID on MQTTlens, clean session determines if broker info is wiped
#userdata = Payload being sent,protocal is version of MQTT, either  MQTTv31 or MQTTv311 (web sockets), transport is declaring the usage of TCP protocal



connect(host, port=1883, keepalive=60, bind_address="mqtt.things.ph") #IP/DNS name to connect to MQTT broker

client.connect(mqtt.things.ph) #