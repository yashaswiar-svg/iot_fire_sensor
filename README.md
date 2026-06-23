# ESP32 Smart Forest System

## Overview
The ESP32 Smart Forest System is an IoT-based fire detection project. It monitors environmental conditions using a digital flame sensor and provides immediate localized alerts via an I2C LCD and a buzzer[cite: 1]. Additionally, it pushes real-time status updates to the Blynk IoT cloud platform for remote monitoring[cite: 1].

## Features
*   **Real-time Monitoring:** Scans for fire hazards every 1 second[cite: 1].
*   **Local Alarms:** Activates a buzzer and updates a 16x2 LCD screen with warning messages upon fire detection[cite: 1].
*   **Cloud Integration:** Connects to the Blynk IoT platform to push status updates to a remote dashboard[cite: 1].
*   **State Management:** Utilizes state-tracking logic to only update the LCD and Cloud when the sensor status changes, reducing screen flickering and network payload[cite: 1].

## Hardware Requirements
*   ESP32 Development Board[cite: 1]
*   Flame Sensor (Digital output)[cite: 1]
*   Active Buzzer[cite: 1]
*   16x2 LCD Display with I2C Module[cite: 1]
*   Jumper wires and Breadboard

## Pin Configuration
| Component    | ESP32 Pin | Logic/Address | Note |
| :---         | :---      | :---          | :--- |
| Flame Sensor | GPIO 19   | Active LOW    | `LOW` indicates fire[cite: 1]. |
| Buzzer       | GPIO 18   | Active HIGH   | `HIGH` sounds the alarm[cite: 1]. |
| I2C LCD      | I2C Pins  | `0x27`        | 16 Columns, 2 Rows[cite: 1]. |

## Software & Library Requirements
Ensure you have the following libraries installed in your Arduino IDE:
*   `WiFi.h` & `WiFiClient.h` (Standard ESP32 Core libraries)[cite: 1]
*   `BlynkSimpleEsp32.h`[cite: 1]
*   `Wire.h`[cite: 1]
*   `LiquidCrystal_I2C.h`[cite: 1]

## Configuration and Setup
1. **Blynk Setup:** Create a template in Blynk named "Firesensor" with the Template ID `TMPL35Cnujr6f`[cite: 1]. Set up a Datastream attached to Virtual Pin `V1` (String format).
2. **Wi-Fi Credentials:** Update the `ssid` and `pass` variables in the code with your local network credentials[cite: 1].
3. **Blynk Token:** Replace `BLYNK_AUTH_TOKEN` with the unique Auth Token provided by your Blynk web dashboard[cite: 1].
4. **Upload:** Compile and upload the code to your ESP32 board.
5. **Monitor:** Open the Serial Monitor at `115200` baud rate to view system initialization and sensor scan logs[cite: 1].
