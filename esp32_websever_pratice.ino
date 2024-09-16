#include <WiFi.h>
#include <WebServer.h>
//Esp32 websever 
//theory: cofig routes,begin
//pratical : conn to same wifi of all device (esp32 ap web device
const char* ssid = "iPhone";
const char* password = "622968143";

// Initialize WebServer on port 80
WebServer server(80);

void setup() {
  // Start serial communication for debugging
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  // Wait for WiFi to connect
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());

  // url
  server.on("/", []() {
    server.send(200, "text/html", "<h1>Hello, World!</h1>");
  });

  // Start the server
  server.begin();
  Serial.println("Server started");
}

void loop() {
  // Handle incoming client requests
  server.handleClient();
}
