from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from datetime import datetime
from multiprocessing import Process
import django
django.setup()

from net_system.models import NetworkDevice     # noqa


def sh_ver(device):
    creds = device.credentials
    remote_conn = ConnectHandler(device_type=device.device_type,
                                 ip=device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=device.port, secret='')
    print(remote_conn.send_command_expect("sh ver"))


def main():
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    procs = []
    for device in devices:
        my_proc = Process(target=sh_ver, args=(device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        print(a_proc)
        a_proc.join()

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()
