#include <Arduino.h>
#include <HTTPClient.h>
#include <WiFi.h>

const int BombaPin = 2;

const char* ssid = "Familia Magaña";  // Tu SSID
const char* password = "Maganavaldes";  //Tu Clave

float hD = 0;
int rain = 0;
int ciclos = 0;

void apiConnection() {
    HTTPClient http;
    http.begin("http://192.168.3.75/ServicioRedNeuronal/iotWaterPump.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    int httpCode = http.GET();

    if (httpCode > 0) {
        Serial.println("Sns HTTP - " + String(httpCode));
        if (httpCode == 200){
            String response = http.getString();
            hD = response.toFloat();
            Serial.println(hD);
        }
    } else {
        Serial.println("HTTP - " + String(httpCode));
    }
    http.end();
}

void apiPrediction() {
    HTTPClient http;
    http.begin("http://192.168.3.75/iot/iotDevicesAPI/iotGetPrediction.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    int httpCode = http.GET();

    if (httpCode > 0) {
        Serial.println("ML HTTP - " + String(httpCode));
        if (httpCode == 200){
            String response = http.getString();
            rain = response.toInt();
            Serial.println(rain);
        }
    } else {
        Serial.println("HTTP - " + String(httpCode));
    }
    http.end();
}

void setup() {
    pinMode(BombaPin, OUTPUT);
    Serial.begin(115200);

    Serial.println("Bomba RL");

    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    Serial.println("");

    // Wait for connection
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.print("Conectado a ");
    Serial.println(ssid);
    Serial.print("Direccion IP: ");
    Serial.println(WiFi.localIP());
    apiPrediction();
    apiConnection();
    delay(5000);
}

void loop() {
    ciclos++;
    apiConnection();

    if (ciclos == 10) {
        apiPrediction();
        ciclos = 0;
    }

    if (rain == 0) {
        if (hD > 60) {
            digitalWrite(BombaPin, LOW);
            Serial.println("Bomba: Off");
        } if (hD < 30) {
            digitalWrite(BombaPin, HIGH);
            Serial.println("Bomba: on");
        }
    } else if (rain != 0 && hD < 10) {
        if (hD > 60) {
            digitalWrite(BombaPin, LOW);
            Serial.println("Bomba: Off");
        } if (hD < 30) {
            digitalWrite(BombaPin, HIGH);
            Serial.println("Bomba: on");
        }
    } else {
        digitalWrite(BombaPin, LOW);
        Serial.println("Bomba: Off");
    }
    delay(5000);
}