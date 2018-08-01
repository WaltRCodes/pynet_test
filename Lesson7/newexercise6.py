from __future__ import print_function, unicode_literals
from napalm import get_network_driver
from my_devices import pynet_rtr1, pynet_sw1, nxos1

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def pingtest(device):
    print("pinging website")
    try:
        ping_output = device.ping(destination='google.com')
    except NotImplementedError:
        print("Ping failed: ping() method not implemented")
        return
    if not ping_output == {}:
        probes_sent = int(ping_output['success']['probes_sent'])
        packet_loss = int(ping_output['success']['packet_loss'])
        successful_pings = probes_sent - packet_loss
        print("Probes sent: {}".format(probes_sent))
        print("Packet loss: {}".format(packet_loss))
        if successful_pings > 0:
            print("Pings Successful: {}".format(successful_pings))
            return
    print("Ping Not Successful")


def main():
    for a_device in (pynet_rtr1, pynet_sw1, nxos1):
        template_vars = {
            'dns1': '1.1.1.1',
            'dns2': '8.8.8.8',
        }

        device_type = a_device.pop('device_type')
        base_dir = '/home/wrada'
        print("{}".format(device_type))
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        device.open()
        device.load_template("dns", template_path=base_dir, **template_vars)
        print(device.compare_config())
        device.commit_config()

        pingtest(device)
        print()

    print()


if __name__ == "__main__":
    main()
