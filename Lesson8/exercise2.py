from __future__ import print_function, unicode_literals
import django
django.setup()
from net_system.models import NetworkDevice


def main():
    devices = NetworkDevice.objects.all()
    for device in devices:
        if 'cisco' in device.device_type:
            device.vendor = 'Cisco'
        elif 'juniper' in device.device_type:
            device.vendor = 'Juniper'
        elif 'arista' in device.device_type:
            device.vendor = 'Arista'
        device.save()

    for device in devices:
        print(device, device.vendor)


if __name__ == "__main__":
    main()
