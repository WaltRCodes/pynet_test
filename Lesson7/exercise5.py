from __future__ import print_function, unicode_literals
from napalm import get_network_driver
from my_devices import pynet_rtr1


def main():
    for a_device in (pynet_rtr1,):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        device.open()

        print("load no commit")
        device.load_merge_candidate(filename='cisco_merge.txt')
        print(device.compare_config())

        print("discard")
        device.discard_config()
        print(device.compare_config())

        print("load commit")
        device.load_merge_candidate(filename='cisco_merge.txt')
        print(device.compare_config())
        device.commit_config()


if __name__ == "__main__":
    main()
