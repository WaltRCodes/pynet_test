from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    password = '88newclass'
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
        a_dict['verbose'] = False

    for a_device in (pynet1, pynet2):
        net_connect = ConnectHandler(**a_device)
        net_connect.send_config_from_file(config_file='config_file.txt')
        nextoutput = net_connect.send_command("show run | inc logging")
        print()
        print("Device: {}:{}".format(net_connect.ip, net_connect.port))
        print(nextoutput)
        print()
if __name__ == "__main__":
    main()
