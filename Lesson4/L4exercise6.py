from __future__ import print_function, unicode_literals
from datetime import datetime
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    password = '88newclass'
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
        a_dict['verbose'] = False

    print("\nStart time: " + str(datetime.now()))
    for a_device in (pynet1, pynet2, juniper_srx):
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command("show arp")
        print()
        print('#' * 80)
        print("Device: {}:{}".format(net_connect.ip, net_connect.port))
        print()
        print(output)
        print('#' * 80)
        print()

    print("\nEnd time: " + str(datetime.now()))


if __name__ == "__main__":
    main()
