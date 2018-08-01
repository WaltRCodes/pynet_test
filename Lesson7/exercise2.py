from __future__ import print_function, unicode_literals
from pprint import pprint
from napalm import get_network_driver
from my_devices import pynet_rtr1, pynet_rtr2

def main():
    for a_device in (pynet_rtr1, pynet_rtr2):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        device.open()
        lldp_info = device.get_lldp_neighbors()
        hostname = a_device['hostname']
        print("{hostname}:\n".format(hostname=hostname))
        pprint(lldp_info)
        print()

if __name__ == "__main__":
    main()
