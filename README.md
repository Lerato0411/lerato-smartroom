![Uploading image.png…]()

 # lerato-smartroom
 ## Table of contents
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

- ## Overview

This project enables automated control of room lighting and fan speed based on ambient light and motion detection. The ESP32 microcontroller collects data from LDR and PIR sensors and communicates with a Flask backend. Users can monitor and override system behavior through a user-friendly Flet-based frontend dashboard.

## Features

- Real-time monitoring of light intensity and motion detection
- Automated control of LED lighting and fan speed
- Manual override capabilities via the frontend dashboard
- Responsive web interface built with Flet
- RESTful API endpoints for seamless communication between components

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
   ```bash
   cd backend
pip install -r requirements.txt
python app.py
2.Navigate to the frontend directory:
cd frontend
pip install flet requests
python main.py


### 9. **Usage**

Explain how to operate the system after installation.

**Example:**
```markdown
## Usage

- Ensure the ESP32 is powered and connected to WiFi.
- Start the Flask backend server.
- Launch the Flet frontend application.
- Use the dashboard to monitor sensor readings and control the LED and fan manually if desired.

## Screenshots

![Dashboard Overview](images/dashboard_overview.png)
*Dashboard displaying real-time sensor data and control options.*

![Hardware Setup](images/hardware_setup.png)
*ESP32 connected with sensors and actuators.*

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.










  



