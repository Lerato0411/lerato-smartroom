![Home Automation Made Easy  Turn your home into a…](https://github.com/user-attachments/assets/4d1d81da-22d9-4192-acec-f9cff67eef8b)

 # lerato-smartroom
 ## Table of contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)

- ## Overview

This project enables automated control of room lighting and fan speed based on ambient light and motion detection. The ESP32 microcontroller collects data from LDR and PIR sensors and communicates with a Flask backend. Users can monitor and override system behavior through a user-friendly Flet-based frontend dashboard.

## Features

- Real-time monitoring of light intensity and motion detection
- Automated control of LED lighting and fan speed
- Manual override capabilities via the frontend dashboard
- Responsive web interface built with Flet

## System Architecture


- **ESP32**: Collects sensor data and sends it to the Flask backend; receives control commands.
- **Flask Backend**: Processes incoming data, applies control logic, and serves API endpoints.
- **Flet Frontend**: Provides a dashboard for users to monitor sensor data and control devices.

## Hardware Requirements

- ESP32 Development Board
- Light Dependent Resistor (LDR)
- Passive Infrared (PIR) Motion Sensor
- LED
- Fan (PWM controllable)
- Resistors and connecting wires
- Breadboard

## Software Requirements

- **ESP32 Firmware**:
  - Arduino IDE
  - WiFi.h
  - HTTPClient.h
  - ArduinoJson.h

- **Backend**:
  - Python 3.x
  - Flask
  - Flask-CORS

- **Frontend**:
  - Python 3.x
  - Flet
  - Requests library

## Installation

### ESP32 Firmware

1. Open the Arduino IDE.
2. Install necessary libraries: WiFi, HTTPClient, ArduinoJson.
3. Load the provided Arduino sketch onto the ESP32.
4. Update WiFi credentials and server URL in the code.

### Flask Backend

1. Navigate to the backend directory:

-cd backend
-pip install -r requirements.txt
-python app.py

2.Navigate to the frontend directory:

 -cd frontend
 -pip install flet requests
 -python main.py

## Usage

- Ensure the ESP32 is powered and connected to WiFi.
- Start the Flask backend server.
- Launch the Flet frontend application.
- Use the dashboard to monitor sensor readings and control the LED and fan manually if desired.

## Screenshots

## Schematic
![Schematic diagram](https://github.com/user-attachments/assets/3e93d4e1-6c07-40ea-888b-154c59bae4c4)

![Dashboard Overview]( )
*Dashboard displaying real-time sensor data and control options.*

![Screenshot 2025-05-14 231316](https://github.com/user-attachments/assets/ea4feaaf-6c87-4748-b142-143d9815ca04)

![Screenshot 2025-05-14 231455](https://github.com/user-attachments/assets/042b29fb-b3cb-4722-83c6-0f55fc37e39b)

![Hardware Setup](images/hardware!)
*ESP32 connected with sensors and actuators.*

![hardware](https://github.com/user-attachments/assets/ed3fbd6d-7fc3-4dc2-9fab-75181cac35b0)

![hardwaree](https://github.com/user-attachments/assets/f3fee3d1-3106-4e39-97c7-7fcb35c79fdf)




## Youtube Link

![mqdefault](https://github.com/user-attachments/assets/dd499b2e-8611-4829-8355-7ff3a94875b1)

https://www.youtube.com/watch?v=kWLnKIRkO7U





  



