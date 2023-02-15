#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <ArduinoJson.h>
#include <Adafruit_Sensor.h>

// wifi user and pass set
const char* ssid = "Li Phone";
const char* password = "abcde12345";

//MQTT broker DNS
const char* mqtt_server = "mqtt.things.ph";
StaticJsonDocument<5000> payload;
StaticJsonDocument<5000> payload_fields;
StaticJsonDocument<200> doc;
char type[20];
long prev =0;
WiFiClient espClient; //begin wifi client instance named espClient
PubSubClient client(espClient); //links pub sub capabilities in the espClient instance
long lastMsg = 0;
char msg[50];
char combo[200];

Adafruit_BMP280 bmp; // initiate class instance bmp to be later called
float temperature = 0;
float pressure = 0;
float altitude = 0;

void setup() {
  Serial.begin(115200); //baud rate esp32s operates on

  if (!bmp.begin(0x76)) {  //I2C address of BMP280
    Serial.println("Could not find a valid BMP280 sensor, check wiring!");
    while (1);
  }
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  //pinMode(ledPin, OUTPUT);
}

void setup_wifi() {
  delay(10);
  // Begin connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
}
/*
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();
*/
/*
  deserializeJson (doc, messageTemp);

  strcpy(type, doc["type"]);
 //type = doc["type"];
 amplitude = doc["amplitude"];
 period = doc["period"];
 duty_cycle = doc["duty_cycle"];

  Serial.println(type);
  Serial.println(amplitude);
  Serial.println(period);
  Serial.println(duty_cycle);
*/
/*
  // If a message is received on the topic esp32/output, you check if the message is either "on" or "off". 
  // Changes the output state according to the message
  if (String(topic) == "Testing") {
   // Serial.print("Changing output to ");
    if(messageTemp == "on"){
      Serial.println("on");
      digitalWrite(ledPin, HIGH);
    }
    else if(messageTemp == "off"){
      Serial.println("off");
      digitalWrite(ledPin, LOW);
    }
  }
}
*/
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("Re-direction broker Calvin","63e964c00317e3273ecc3165","PQ6xg1TCIKTuSf0QgpFER7c3")) //Connection name,user,password set
    {
      Serial.println("connected");
      // Subscribe
      client.subscribe("Testing");
     
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  
  if (now - lastMsg > 500) {
    lastMsg = now;
    
    payload_fields["temperature"] = bmp.readTemperature();
    payload_fields["pressure"] = bmp.readPressure()/1000;
    payload_fields["altitude"] = bmp.readAltitude();
    /*
    payload_fields["led"] = 0;
    payload_fields["switch"] = 0;
    payload_fields["payload_fields"] = 1;
    payload_fields["Square"] = voltsquare;
    payload_fields["Triangle"] = 0;
*/
    payload["hardware_serial"] = "ESP_32";
    payload["payload_fields"] = payload_fields;
    
    serializeJson(payload, combo);
    Serial.println(combo);    
    client.subscribe("Random_Nums");
    //Serial.println(combo);
    client.publish("Testing", combo);
    
    
   
  }
}