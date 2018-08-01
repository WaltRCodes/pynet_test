from __future__ import print_function, unicode_literals
from napalm import get_network_driver
from my_devices import pynet_sw2


def checkstatus(intf_data):
    if intf_data['is_enabled'] and intf_data['is_up']:
        return True
    return False


def main():
    for a_device in (pynet_sw2,):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        device.open()
        hostname = a_device['hostname']
        print("{hostname}:\n".format(hostname=hostname))

        intf_info = device.get_interfaces()

        print()
        print("Interfaces in an Up/Up state ")
        intf_list = []
        for intf_name, intf_data in intf_info.items():
            if checkstatus(intf_data):
                intf_list.append(intf_name)
        intf_list.sort()
        for intf in intf_list:
            print(intf)

    print()


if __name__ == "__main__":
    main()
