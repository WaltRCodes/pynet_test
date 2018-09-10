from __future__ import print_function, unicode_literals
import django
django.setup()
from net_system.models import NetworkDevice

def main():
    try:
        test_rtr1 = NetworkDevice.objects.get(device_name='test-rtr1')
        test_rtr2 = NetworkDevice.objects.get(device_name='test-rtr2')
        test_rtr1.delete()
        test_rtr2.delete()
    except NetworkDevice.DoesNotExist:
        pass
    print()
    devices = NetworkDevice.objects.all()
    for device in devices:
        print(device)
    print()


if __name__ == "__main__":
    main()
