from __future__ import print_function, unicode_literals
from pynxos.device import Device
from getpass import getpass

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    password = '88newclass'
    nxos1 = {
        'host': 'nxos1.twb-tech.com',
        'username': 'pyclass',
        'password': password,
        'transport': 'https',
        'port': 8443,
    }
    nxos2 = {   # noqa
        'host': 'nxos2.twb-tech.com',
        'username': 'pyclass',
        'password': password,
        'transport': 'https',
        'port': 8443,
    }

    config_commands = ['interface Loopback23', 'ip address 172.31.254.99/32']
    for device in (nxos1,):
        nxapi_conn = Device(**device)
        nxapi_conn.config_list(config_commands)
        output = nxapi_conn.show('show run interface loopback23', raw_text=True)
        print(output)


if __name__ == "__main__":
    main()
