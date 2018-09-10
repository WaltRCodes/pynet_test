from __future__ import print_function, unicode_literals
from datetime import datetime
from netmiko import ConnectHandler
import django
django.setup()
from net_system.models import NetworkDevice 


def show_version(device):
    creds = device.credentials
    remote_conn = ConnectHandler(device_type=device.device_type,
                                 ip=device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=device.port, secret='')
    print(remote_conn.send_command_expect("show version"))


def main():
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()
    for device in devices:
        show_version(device)

    elapsed_time = datetime.now() - start_time
    print("Elapsed time: {}".format(elapsed_time))


if __name__ == "__main__":
    main()
