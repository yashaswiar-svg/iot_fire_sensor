#define BLYNK_TEMPLATE_ID   "TMPL35Cnujr6f"
#define BLYNK_TEMPLATE_NAME "Firesensor"
#define BLYNK_AUTH_TOKEN    "Fe6X_hUYEYU_ElFCzy6iVual2lIeI-Ev"

#define BLYNK_PRINT Serial 

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// WiFi Credentials
char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Abhi";
char pass[] = "10987654321";

// ESP32 Pins
const int FLAME_PIN = 19;  
const int BUZZER_PIN = 18; 

// Initialize LCD (Address 0x27, 16 Columns, 2 Rows)
LiquidCrystal_I2C lcd(0x27, 16, 2); 
BlynkTimer timer;

// Set initial state to true so the setup forced-refresh triggers standard "Safe" display
bool lastState = true; 

void checkFireStatus() {
  int isFireDetected = digitalRead(FLAME_PIN);

  // Debugging log to Serial Monitor
  Serial.print("[Sensor Scan] Value: ");
  Serial.println(isFireDetected == LOW ? "FLAME DETECTED! 🔥" : "Safe... 👍");

  if (isFireDetected == LOW) { 
    digitalWrite(BUZZER_PIN, HIGH); // Activate local alarm
    
    if (lastState == false) {
      Blynk.virtualWrite(V1, "FIRE DETECTED!"); 
      
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("!!! WARNING !!!");
      lcd.setCursor(0, 1);
      lcd.print("FIRE DETECTED!");
      
      lastState = true;
    }
  } else {
    digitalWrite(BUZZER_PIN, LOW); // Deactivate local alarm
    
    if (lastState == true) {
      Blynk.virtualWrite(V1, "Forest Safe"); 
      
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("System Monitored");
      lcd.setCursor(0, 1);
      lcd.print("Status: Safe    ");
      
      lastState = false;
    }
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("\n--- ESP32 SMART FOREST SYSTEM INITIALIZING ---");

  pinMode(FLAME_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);
  
  // Initialize LCD Screen
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Connecting WiFi...");

  // Establish Network and Blynk Connections
  Blynk.begin(auth, ssid, pass);

  // Set up execution timer to check sensor status every 1000ms (1 second)
  timer.setInterval(1000L, checkFireStatus);
  
  // Run immediate status check to baseline the LCD display and cloud state
  checkFireStatus();
  
  Serial.println("--- System Initialization Complete ---");
}

void loop() {
  Blynk.run();
  timer.run();
}