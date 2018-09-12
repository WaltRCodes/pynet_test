from __future__ import print_function, unicode_literals
from napalm import get_network_driver
from email_helper import send_mail


def main():

    srx1 = {
        'device_type': 'junos',
        'hostname': 'srx1.twb-tech.com',
        'username': 'pyclass',
        'password': '88newclass',
        'optional_args': {},
    }

    for net_device in (srx1,):
        device_type = net_device.pop('device_type')
        driver = get_network_driver(device_type)

        device = driver(**net_device)
        device.open()
        lldp_neighbors = device.get_lldp_neighbors()

        for local_intf, lldp_list in lldp_neighbors.items():
            remote_lldp = lldp_list[0]
            remote_host = remote_lldp['hostname']
            remote_port = remote_lldp['port']
            break

        msg = """
SRX1 is connected on local intf: {local_intf}
To remote host: {remote_host} On remote port: {remote_port}
""".format(local_intf=local_intf, remote_host=remote_host, remote_port=remote_port)

        recipient = 'walter.rada@mail.citytech.cuny.edu'
        sender = 'twb@twb-tech.com'
        subject = 'Bonus lesson LLDP exercise'
        send_mail(recipient, subject, message=msg, sender=sender)
        print("message sent")


if __name__ == "__main__":
    main()
