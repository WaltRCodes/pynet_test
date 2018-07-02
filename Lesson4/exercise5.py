from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx


def main():
    password = '88newclass'
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
    net_connect2 = ConnectHandler(**pynet2)
    net_connect2.config_mode()
    print("\n")
    print("Config mode check: {}".format(net_connect2.check_config_mode()))
    print("Current prompt: {}".format(net_connect2.find_prompt()))
    print("\n")


if __name__ == "__main__":
    main()
