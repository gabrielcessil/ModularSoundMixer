# Modmixer

A modular sound controller designed for Linux applications. This project covers hardware development, embedded software, and a graphical interface to provide seamless volume control for multiple applications on your desktop.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Known Issues](#known-issues)
- [Contributors](#contributors)
- [License](#license)

## About the Project
**Modmixer** is a low-cost, modular sound controller for Linux desktops, allowing users to adjust the volume of individual applications using physical modules connected via USB. The project integrates CAD modeling, electronic assembly, serial communication, and GUI development.

## Features
- **Graphical Interface**: Easily assign applications to modules.
- **Modular Control**: Increase or decrease the volume of specific applications.
- **Plug and Play**: Automatic recognition of modules upon connection.
- **Scalability**: Supports varying numbers of modules.
- **Single USB Connection**: All data transmitted via one USB port.

## Getting Started

### Prerequisites
- **Operating System**: Linux (tested on Ubuntu 20.04 LTS)
- **Hardware**: ESP8266 module ESP-01, USB adapter for ESP-01
- **Software Dependencies**: Listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/modmixer.git
   cd modmixer
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Connect the main module to your USB port.

## Usage
Run the interface using:
```bash
python main.py
```
The system will detect connected modules and allow application assignment through the GUI.

## Project Structure
- **Interface Gráfica**: Developed with PySimpleGUI.
- **Comunicacão Serial**: Manages communication between modules and the computer via USB.
- **Eletroônica e Montagem**: Assembled using ESP8266 modules and custom PCBs.
- **Modelagem CAD**: Designed enclosures using additive manufacturing techniques (3D printing with PLA).

## Testing

### Interface Testing
- **Information Capture**: Validates data transmission from modules.
- **Module Detection**: Ensures GUI updates based on connected modules.
- **Application Selection**: Tests correct mapping between physical modules and applications.
- **Audio Control**: Verifies real-time volume adjustments.
- **Delay Measurement**: Measures response time between input and system action.

### Serial Communication Testing
- **Module Detection & Address Assignment**: Validates I2C communication and address allocation.
- **Message Integrity**: Checks data consistency in communication.
- **Volume Variation**: Monitors volume adjustment accuracy.

## Known Issues
- **PySimpleGUI Bugs**: Unexpected behavior with interface closing events.
- **PySerial Readline**: Inconsistent timeout handling, resolved using `read_until`.
- **Documentation Gaps**: Delay handling between write and read operations in PySerial.

## Contributors
- **Guilherme Turatto** - Serial Communication
- **Gabriel Cesar Silveira** - Graphical Interface

---

*This project was developed as part of the Integrative Project II at the Federal University of Santa Catarina, Joinville Technological Campus.*

