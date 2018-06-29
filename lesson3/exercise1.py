from __future__ import print_function, unicode_literals
import cPickle as pickle
import os.path
from datetime import datetime
from getpass import getpass
from collections import namedtuple
import json
import yaml
from snmp_helper import snmp_get_oid_v3, snmp_extract
from email_helper import send_mail



NetworkDevice = namedtuple("NetworkDevice", "time last_changed run_config_changed")

def obtain_objects(filename):
    net_dev = {}

    if not os.path.isfile(filename):
        return{}

    if filename.count(".") == 1:
        out_format = filename.split(".")
    else:
        raise ValueError("Invalid file name: {0}".format(filename))
    
    if out_format == 'pk1':
        with open(filename, 'rb') as f:
            while True:
                try:
                    net_dev = cPickle.load(f)
                except EOFError:
                    break
    elif out_format == 'yml':
        with open(filename, 'r') as f:
            net_dev = yaml.load(f)

    elif out_format == 'json':
        with open(filename, 'r') as f:
            net_dev = json.load(f)
            for device_name, device_attrs in net_devices.items():
                uptime, last_changed, run_config_changed = device_attrs
                tmp_device = NetworkDevice(uptime, last_changed, run_config_changed)
                net_devices[device_name] = tmp_device
    else:
        raise ValueError("Invalid filename: {}".format(filename))

    return net_dev

def save_objects(filename, datadictionary):

    if filename.count(".") == 1:
        _, out_format = filename.split(".")
    else:
        raise ValueError("Bad file name: {}".format(filename))

    if out_format == 'pkl':
        with open(filename, 'wb') as f:
            pickle.dump(datadictionary, f)
    elif out_format == 'yml':
        with open(filename, 'w') as f:
            f.write(yaml.dump(datadictionary, default_flow_style=False))
    elif out_format == 'json':
        with open(filename, 'w') as f:
            json.dump(datadictionary, f)


def notifications(device_name):

    current_time = datetime.now()

    sender = '4wrada@gmail.com'
    recipient = '4wrada@gmail.com'
    subject = '{} was modified'.format(device_name)
    message = '''{} was modified at: {}'''.format(device_name, current_time)

    if send_mail(recipient, subject, message, sender):
        print('Email notification sent to {}'.format(recipient))
        return True


def snmp_sysname(a_device, snmp_user):
    return snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid= '1.3.6.1.2.1.1.5.0'))


def snmp_uptime(a_device, snmp_user):
    return int(snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid='1.3.6.1.2.1.1.3.0')))


def create_new_device(device_name, uptime, last_changed):
    dots_to_print = (35 - len(device_name)) * '.'
    print("{} {}".format(device_name, dots_to_print), end=' ')
    print("saving new device")
    return NetworkDevice(uptime, last_changed, False)


def check_for_reboot(saved_device, uptime, last_changed):
    return uptime < saved_device.uptime or last_changed < saved_device.last_changed


def main():
    reload_window = 180 * 100

    net_dev_file = 'netdev.pkl'

 
    rtr1_ip_addr = '184.105.247.70'
    rtr2_ip_addr = '184.105.247.71'
    my_key = 'galileo1'

    snmp_user = ('pysnmp', my_key, my_key)
    pynet_rtr1 = (rtr1_ip_addr, 161)
    pynet_rtr2 = (rtr2_ip_addr, 161)

    print('\n*** Checking for device changes ***')
    saved_devices = obtain_objects(net_dev_file)
    print("{} devices were previously saved\n".format(len(saved_devices)))

    current_devices = {}

    for a_device in (pynet_rtr1, pynet_rtr2):
        device_name = snmp_sysname(a_device, snmp_user)
        uptime = snmp_uptime(a_device, snmp_user)
        last_changed = int(snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.1.0')))
        print("\nConnected to device = {}".format(device_name))
        print("Last changed timestamp = {}".format(last_changed))
        print("Uptime = {}".format(uptime))

        if device_name not in saved_devices:
            current_devices[device_name] = create_new_device(device_name, uptime, last_changed)
        else:
            saved_device = saved_devices[device_name]
            dots_to_print = (35 - len(device_name)) * '.'
            print("{} {}".format(device_name, dots_to_print), end=' ')

            if check_for_reboot(saved_device, uptime, last_changed):
                if last_changed <= reload_window:
                    print("DEVICE RELOADED...not changed")
                    current_devices[device_name] = NetworkDevice(uptime, last_changed, False)
                else:
                    print("DEVICE RELOADED...and changed")
                    current_devices[device_name] = NetworkDevice(uptime, last_changed, True)
                    notifications(device_name)

            elif last_changed == saved_device.last_changed:
                print("not changed")
                current_devices[device_name] = NetworkDevice(uptime, last_changed, False)

            elif last_changed > saved_device.last_changed:
                print("CHANGED")
                current_devices[device_name] = NetworkDevice(uptime, last_changed, True)
                notifications(device_name)
            else:
                raise ValueError()

    save_objects(net_dev_file, current_devices)
    print()


if __name__ == '__main__':
    main()

