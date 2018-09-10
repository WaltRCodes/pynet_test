from __future__ import print_function, unicode_literals
import django
django.setup()
from net_system.models import NetworkDevice     # noqa


def main():

    test_rtr1 = NetworkDevice(
        device_name='test-rtr1',
        device_type='cisco_ios',
        ip_address='184.105.247.70',
        port=5022,
    )
    test_rtr1.save()

    NetworkDevice.objects.get_or_create(
        device_name='test-rtr2',
        device_type='cisco_ios',
        ip_address='184.105.247.71',
        port=5122,
    )
    print()
    devices = NetworkDevice.objects.all()
    for device in devices:
        print(device)
    print()


if __name__ == "__main__":
    main()
