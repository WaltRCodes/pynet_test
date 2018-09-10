from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from datetime import datetime
import threading

import django
django.setup()
from net_system.models import NetworkDevice


def sh_ver(device):
  
    creds = device.credentials
    remote_conn = ConnectHandler(device_type=device.device_type, ip=device.ip_address, username=creds.username, password=creds.password, port=device.port, secret='')
    print(remote_conn.send_command_expect("sh ver"))
    remote_conn.disconnect()


def main():
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for device in devices:
        my_thread = threading.Thread(target=sh_ver, args=(device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()
