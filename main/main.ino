#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverUrl = "http://<backend-ip>:5000";

#define LDR_PIN 34
#define PIR_PIN 27
#define LED_PIN 26
#define FAN_PIN 25
#define TEMP_KNOB_PIN 35

bool overrideLED = false;
bool overrideFan = false;
int manualLEDState = 0;
int manualFanSpeed = 0;

void setup() {
  Serial.begin(115200);
  pinMode(PIR_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  ledcAttach(FAN_PIN, 5000, 8);
  connectWiFi();
}

void loop() {
  int ldr = analogRead(LDR_PIN);
  int pir = digitalRead(PIR_PIN);
  int tempKnob = analogRead(TEMP_KNOB_PIN);

  if (!overrideLED)
    digitalWrite(LED_PIN, (ldr < 1000 && pir) ? HIGH : LOW);
  else
    digitalWrite(LED_PIN, manualLEDState);

  if (!overrideFan) {
    int speed = pir ? map(tempKnob, 0, 4095, 100, 255) : 0;
    ledcWrite(0, speed);
  } else {
    ledcWrite(0, manualFanSpeed);
  }

  sendSensorData(ldr, pir);
  fetchControl();
  delay(5000);
}

void connectWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(1000);
}

void sendSensorData(int ldr, int pir) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(String(serverUrl) + "/update");
    http.addHeader("Content-Type", "application/json");
    String payload = "{\"ldr\":" + String(ldr) + ",\"pir\":" + String(pir) + "}";
    http.POST(payload);
    http.end();
  }
}

void fetchControl() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(String(serverUrl) + "/control");
    int httpCode = http.GET();
    if (httpCode == 200) {
      String body = http.getString();
      DynamicJsonDocument doc(512);
      deserializeJson(doc, body);
      overrideLED = doc["overrideLED"];
      overrideFan = doc["overrideFan"];
      manualLEDState = doc["ledState"];
      manualFanSpeed = doc["fanSpeed"];
    }
    http.end();
  }
}
