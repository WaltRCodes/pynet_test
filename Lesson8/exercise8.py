from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from datetime import datetime
from multiprocessing import Process, Queue

import django
django.setup()

from net_system.models import NetworkDevice


def sh_ver_queue(device, outputqueue):
    output_dict = {}
    creds = device.credentials
    remote_conn = ConnectHandler(device_type=device.device_type,
                                 ip=device.ip_address,
                                 username=creds.username, password=creds.password,
                                 port=device.port, secret='', verbose=False)
    output = "\n"
    output += remote_conn.send_command_expect("sh ver")
    output_dict[device.device_name] = output
    outputqueue.put(output_dict)


def main():
    start_time = datetime.now()
    outputqueue = Queue(maxsize=20)
    devices = NetworkDevice.objects.all()

    procs = []
    for device in devices:
        my_proc = Process(target=sh_ver_queue, args=(device, outputqueue))
        my_proc.start()
        procs.append(my_proc)
    for a_proc in procs:
        a_proc.join()

    while not outputqueue.empty():
        my_dict = outputqueue.get()
        for k, val in my_dict.items():
            print(k)
            print(val)

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()
