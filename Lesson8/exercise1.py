from __future__ import print_function, unicode_literals
import django
django.setup()
from net_system.models import NetworkDevice, Credentials   


def main():
    devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    std = creds[0]
    arista = creds[1]

    for device in devices:
        if 'arista' in device.device_type:
            device.credentials = arista
        else:
            device.credentials = std
        device.save()

    for device in devices:
        print(device, device.credentials)


if __name__ == "__main__":
    main()
