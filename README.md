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
- [Technical Details](#technical-details)
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

## Technical Details

### Functional Requirements
- **RF1**: Possess a graphical interface for configuring hardware modules.
- **RF2**: Users must be able to control the volume of different applications from the modules.
- **RF3**: Plug and play functionality.
- **RF4**: Ensure functionality with different numbers of modules.
- **RF5**: Transmit module information to the computer via a single USB connection.

### Non-Functional Requirements
- **RNF 1.1**: USB port selection box for connecting to the main module.
- **RNF 1.2**: Selection box to link each connected module to the desired application.
- **RNF 1.3**: The number of selection boxes displayed should match the number of connected modules.
- **RNF 1.4**: Display a warning screen if no module is connected.
- **RNF 1.5**: Display a progress bar to indicate the current application volume.
- **RNF 1.6**: Button to terminate the interface execution.
- **RNF 2.1**: The connection sequence of the modules should correspond to the sequence of indices listed vertically in the graphical interface.
- **RNF 2.2**: The potentiometer’s minimum and maximum limits should be translated to the application’s audio levels.
- **RNF 2.3**: Application selection in the interface should only modify the selected application's volume.
- **RNF 3.1**: Define I2C protocol addresses at runtime via auxiliary communication based on the One-Wire protocol.
- **RNF 3.2**: Each module should signal to the main device if there is a subsequent module connected and its address.
- **RNF 3.3**: The main device should store the number of connected devices and their respective addresses.
- **RNF 4.1**: The main device should update the list of connected devices whenever a request is not met twice consecutively.
- **RNF 4.2**: The main module should notify the user interface program whenever there are changes in the list of connected devices.
- **RNF 4.3**: The 3.3V power bus (VCC and GND) and the I2C bus (SCL and SDA) should have a direct path between the modules and the main device.
- **RNF 5**: The main module should contain a USB adapter for the ESP01 microcontroller.
- **RNF 5.1**: Serial communication between the master module and the computer via USB at 9600bps.
- **RNF 5.2**: Communication between the main module and other modules via I2C.
- **RNF 5.3**: The main module should periodically request status (volume) from secondary modules at a maximum interval of 50 milliseconds.
- **RNF 5.4**: The main module should send the status of all modules to the computer periodically at a maximum interval of 100 milliseconds.

### Development Assumptions
- **Operating System**: Linux (Ubuntu 20.04 LTS) with all necessary dependencies installed.
- **Microcontroller**: ESP8266 module ESP-01 for all modules.
- **Connection**: Between the main module and the computer through a USB adapter designed for ESP-01 (ESP01-USB).
- **Module Limits**: 
  - **USB 2.0 (500mA)**: Main module + 4 Modules.
  - **USB 3.0 (900mA)**: Main module + 8 Modules.

### CAD Modeling and Case Printing
- **Initial Fit Tests**: Conducted to optimize the project timeline before final assembly.
- **Design Specifications**: 
  - 2mm thickness for cases for sufficient mechanical strength.
  - Dimensions: 44mm width and 100mm length (later reduced).
- **Material**: PLA for cost-effectiveness and low melting point.
- **Printing Details**: 
  - Initial modules used 51g of material.
  - 7 hours print time per module.
- **Final Adjustments**: Position of potentiometers changed to the top, and a logo was added to the cases.

## Testing

### Interface Testing
1. **Information Capture**: Validates data transmission from modules using Arduino Nano to emulate control signals.
2. **Module Detection**: Ensures GUI updates based on connected modules and tests detection accuracy.
3. **Application Selection**: Verifies correct mapping and volume control for selected applications.
4. **Audio Control**: Confirms the alignment of system audio levels with control signals.
5. **Delay Measurement**: Measures response time from control signal capture to system sound adjustment.

### Serial Communication Testing
1. **Module Detection & Address Assignment**: Ensures proper communication using I2C and correct address allocation.
2. **Message Integrity**: Checks for consistency in message size and checksum validation.
3. **Volume Variation**: Monitors accuracy in volume adjustments.

## Known Issues
- **PySimpleGUI Bugs**: Issues with interface closing events due to recent updates.
- **PySerial Readline**: Inconsistent timeout handling, resolved using `read_until`.
- **Delay Handling**: Lack of documentation on delay between read and write operations caused initial failures.

## Contributors
- **Guilherme Turatto** - Serial Communication
- **Gabriel Cesar Silveira** - Graphical Interface

## License
Distributed under the MIT License. See `LICENSE` for more information.

---

*This project was developed as part of the Integrative Project II at the Federal University of Santa Catarina, Joinville Technological Campus.*

