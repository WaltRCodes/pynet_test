from __future__ import print_function, unicode_literals
from napalm import get_network_driver
from my_devices import pynet_rtr1


def getbgpneighbor(bgp_data, neighbor):
    return bgp_data['global']['peers'][neighbor]


def main():
    for a_device in (pynet_rtr1,):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        device.open()
        hostname = a_device['hostname']
        print("{hostname}:\n".format(hostname=hostname))
        bgp_info = device.get_bgp_neighbors()
        bgp_neighbor = '10.220.88.38'
        bgp_neighbor_dict = getbgpneighbor(bgp_info, bgp_neighbor)
        bgp_state = bgp_neighbor_dict['is_up']
        print("BGP Neighbor: {}, BGP Established State: {}".format(bgp_neighbor, bgp_state))
        print()


if __name__ == "__main__":
    main()
