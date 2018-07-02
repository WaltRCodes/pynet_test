from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    password = '88newclass'
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
        a_dict['verbose'] = False
    net_connect = ConnectHandler(**pynet2)
    config_commands = ['logging buffered 20000']
    net_connect.send_config_set(config_commands)
    nextoutput = net_connect.send_command("show run | inc logging buffer")
    print("Device: {}:{}".format(net_connect.ip, net_connect.port))
    print()
    print(nextoutput)


if __name__ == "__main__":
    main()
