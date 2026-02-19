# BLE RSSI-based Distance Estimation System

## Overview

This project implements a Bluetooth Low Energy (BLE) RSSI scanner using Python and BlueZ on Raspberry Pi.

It collects RSSI (Received Signal Strength Indicator) values from nearby BLE devices and applies a Moving Average Filter to reduce signal noise. The filtered RSSI data is stored for distance estimation and signal analysis.

This system was developed as part of an RSSI-based indoor distance estimation research project.

---

## Key Features

- BLE device discovery using BlueZ Bluetooth stack
- Real-time RSSI data collection
- Moving Average Filter implementation for noise reduction
- Event-driven architecture using D-Bus
- RSSI logging system

---

## Technology Stack

- Language: Python
- Platform: Raspberry Pi (Linux)
- Bluetooth Stack: BlueZ
- Library: pydbus
- Architecture: Event-driven system

---

## System Architecture

BLE Device  
↓  
BlueZ Stack  
↓  
pydbus  
↓  
RSSI Collection  
↓  
Moving Average Filter  
↓  
Log Storage  

---

## Core Implementation

### RSSI Filtering

Moving Average Filter was implemented to reduce RSSI signal fluctuations.

```python
def apply_moving_average(rssi):
    rssi_window.append(rssi)
    if len(rssi_window) > window_size:
        rssi_window.pop(0)
    return sum(rssi_window) / len(rssi_window)

## Project Demo

This project was tested on Raspberry Pi using BlueZ Bluetooth stack to collect RSSI values from BLE devices.

Example log output:

```
[12:01:22] Device: AA:BB:CC:DD:EE:FF, RSSI: -65.40 dBm
[12:01:23] Device: AA:BB:CC:DD:EE:FF, RSSI: -64.80 dBm
[12:01:24] Device: AA:BB:CC:DD:EE:FF, RSSI: -65.10 dBm
```

## Repository Structure

```
ble-rssi-distance-estimator/
├── rssi_scanner.py
├── README.md
└── .gitignore
```
