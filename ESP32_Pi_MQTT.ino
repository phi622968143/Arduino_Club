#include <PubSubClient.h>
#include <WiFi.h>  
const char* ssid = "";
const char* password = "";
const char* mqttServer = ""; 
const int mqttPort = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("Connected to WiFi");

    client.setServer(mqttServer, mqttPort);
    
    while (!client.connected()) {
        Serial.println("Connecting to MQTT...");
        if (client.connect("ESP32Client")) {
            Serial.println("Connected!");
        } else {
            Serial.print("Failed with state ");
            Serial.println(client.state());
            delay(2000);
        }
    }
}

void loop() {
    if (!client.connected()) {
        client.connect("ESP32Client");
    }
    client.publish("esp32/data", "Hello from ESP32!");
    Serial.println("Message sent!");
    delay(5000);
}
