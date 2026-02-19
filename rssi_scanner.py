"""
BLE RSSI Scanner
Author: Seonghyeon Yun

Description:
Bluetooth RSSI 값을 수집하고 Moving Average Filter를 적용하여
노이즈를 줄인 RSSI 데이터를 로그 파일로 저장하는 프로그램.
"""

import pydbus
from gi.repository import GLib
from datetime import datetime

# RSSI moving average filter
rssi_window = []
window_size = 5

# 로그 파일 생성
log_file = open("rssi_log.txt", "a")


def apply_moving_average(rssi):

    rssi_window.append(rssi)

    if len(rssi_window) > window_size:
        rssi_window.pop(0)

    avg_rssi = sum(rssi_window) / len(rssi_window)

    return avg_rssi


def write_to_log(address, rssi):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"[{current_time}] Device: {address}, RSSI: {rssi:.2f} dBm\n"

    print(log)

    log_file.write(log)

    log_file.flush()


class DeviceMonitor:

    def __init__(self, bus, device_path):

        self.device = bus.get('org.bluez', device_path)

        self.device.onPropertiesChanged = self.properties_changed


    def properties_changed(self, interface, changed, invalidated):

        if 'RSSI' in changed:

            rssi = changed['RSSI']

            filtered_rssi = apply_moving_average(rssi)

            write_to_log(self.device.Address, filtered_rssi)


def main():

    bus = pydbus.SystemBus()

    adapter = bus.get('org.bluez', '/org/bluez/hci0')

    adapter.StartDiscovery()

    print("BLE RSSI Scanner Started...")

    loop = GLib.MainLoop()

    loop.run()


if __name__ == "__main__":
    main()
