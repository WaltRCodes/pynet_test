from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler

pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'host': 'cisco2.twb-tech.com',
    'username': 'pyclass',
    'password': '88newclass',
}

net_connect = ConnectHandler(**pynet_rtr2)
show_ip = net_connect.send_command('show ip int brief', use_textfsm=True)

for interface_dictionary in show_ip:
    if interface_dictionary['intf'] == 'FastEthernet4':
        print("IP address of FA4: {ipaddr}".format(**interface_dictionary))

