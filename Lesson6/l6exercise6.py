from __future__ import print_function, unicode_literals
from pynxos.device import Device
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def processrtable(table):
    table = table['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']
    return table['TABLE_prefix']['ROW_prefix']


def nexthop(entry):
    data = entry['TABLE_path']['ROW_path']
    return data['ipnexthop']


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

    print()
    for device in (nxos1,):
        nxapi_conn = Device(**device)
        print('-' * 40)
        table = nxapi_conn.show('show ip route vrf management')
        table = processrtable(table)
        for entry in table:
            if entry['ipprefix'] == '0.0.0.0/0':
                next_hop = nexthop(entry)
                print("Default Gateway: {}".format(next_hop))
                break
        print('-' * 40)
    print()


if __name__ == "__main__":
    main()
