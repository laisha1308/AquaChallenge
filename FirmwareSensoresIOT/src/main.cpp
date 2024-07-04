#include <Arduino.h>
#include <DHT.h>
#include <WiFi.h>
#include <WebServer.h>
#include <HTTPClient.h>
#include <LiquidCrystal_I2C.h>
#include <Adafruit_BME280.h>

#define DHTTYPE DHT22
Adafruit_BME280 bme;

const int lcdColumns = 16;
const int lcdRows = 2;
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);

const int BombaPin = 2;
const int DHTPin = 5;
const int FCPin = 34;

DHT dht(DHTPin, DHTTYPE);

const char* ssid = "SAMI-LAISHA";  // Tu SSID
const char* password = "lluvia1972";  //Tu Clave
WebServer server(80);

float hD = 0;
float hA = 0;
float t = 0;
float p = 0;

void handle_NotFound() {
    server.send(404, "text/plain", "La pagina no existe");
}

String SendHTML() {
    // Cabecera de todas las paginas WEB
    String ptr = "<!DOCTYPE html> <html>\n";

    // <meta> viewport. Para que la pagina se vea correctamente en cualquier dispositivo
    ptr += "<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\", charset=\"UTF-8\">\n";
    ptr += "<title>Control Humedad</title>\n";
    ptr += "<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
    ptr += "body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n";
    ptr += ".button {display: block;width: 80px;background-color: #3498db;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto 35px;cursor: pointer;border-radius: 4px;}\n";
    ptr += "p {font-size: 20px;color: #888;margin-bottom: 10px;}\n";
    ptr += "</style>\n";
    ptr += "<script>function refreshPage() { location.reload(); }</script>\n"; // Script de actualización
    ptr += "</head>\n";
    ptr += "<body>\n";
    /*
     * Encabezados de la pagina
     */
    ptr += "<h1>ESP32 WEB Server</h1>\n";

    ptr += "<p>Temperatura: ";
    ptr += t;
    ptr +=" °C</p>";

    ptr += "<p>Humedad en tierra: ";
    ptr += hD;
    ptr +="%</p>";

    ptr += "<p>Humedad en aire: ";
    ptr += hA;
    ptr +="%</p>";

    ptr += "<script>setTimeout(refreshPage, 1000);</script>\n"; // Actualiza cada 5 segundos
    ptr += "</body>\n";
    ptr += "</html>\n";
    return ptr;
}

void handle_OnConnect() {
    server.send(200, "text/html", SendHTML());
}

void apiConection() {
    HTTPClient http;
    String data = "ha=" + String(hA) + "&hd=" + String(hD) + "&t=" + String(t) + "&p=" + String(p);
    http.begin("http://192.168.137.19/ServicioRedNeuronal/iotDataSensors.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    int httpCode = http.POST(data);

    if (httpCode > 0) {
        Serial.println("HTTP - " + String(httpCode));
        if (httpCode == 200){
            String request = http.getString();
            Serial. println (request);
        }
    } else {
        Serial.println("HTTP - " + String(httpCode));
    }
    http.end();
}

void setup() {
    pinMode(BombaPin, OUTPUT);
    Serial.begin(115200);
    lcd.init();
    lcd.backlight();

    Serial.println("Sensores RL");
    dht.begin();

    if (!bme.begin()) {
        Serial.println("No se pudo encontrar el sensor BME280");
        while (1);
    }

    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    Serial.println("");
    int intento = 0;
    // Wait for connection
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
        lcd.setCursor(0, 0);
        lcd.print("Buscando red:");
        lcd.setCursor(0, 1);
        lcd.println(ssid);
        if (intento >= 20)
            break;
        intento++;
    }
    if (WiFi.status() == WL_CONNECTED) {
        lcd.clear();
        Serial.println("");
        Serial.print("Conectado a ");
        Serial.println(ssid);
        Serial.print("Direccion IP: ");
        Serial.println(WiFi.localIP());
        lcd.setCursor(0, 0);
        lcd.print("Direccion IP:");
        lcd.setCursor(0, 1);
        lcd.println(WiFi.localIP());

        server.on("/", handle_OnConnect); // 1
        server.onNotFound(handle_NotFound); // 3

        server.begin();
        Serial.println("Servidor HTTP iniciado");
        delay(5000);
    }
}

void loop() {
    hD = map(analogRead(FCPin), 0, 4095, 100, 0);
    hA = dht.readHumidity();
    t = dht.readTemperature();
    server.handleClient();

    if (hD > 50) {
        digitalWrite(BombaPin, LOW);
    } else {
        digitalWrite(BombaPin, HIGH);
    }

    delay(2500);
    lcd.clear();
    if (isnan(hA) || isnan(t)) {
        lcd.setCursor(0, 0);
        lcd.println("Failed to read from DHT sensor!");
        Serial.print("Failed to read from DHT sensor!");
        return;
    }
    lcd.setCursor(0, 0);
    lcd.print("Humedad:");
    lcd.setCursor(0, 1);
    lcd.print(hA);
    lcd.print("% ");
    lcd.print(hD);
    lcd.print("%");

    delay(2500);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Temperatura: ");
    lcd.setCursor(0, 1);
    lcd.print(t);
    lcd.print(" *C");
    p = bme.readPressure()/100;
    apiConection();
}