
from __future__ import print_function, unicode_literals
import yaml
from netmiko import ConnectHandler, file_transfer


def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)


def main():

    filename = 'devices.yml'
    my_devices = read_yaml(filename)

    for hostname, net_device in my_devices.items():
        file_system = net_device.pop('file_system')
        net_device['password'] = '88newclass'

        ssh_conn = ConnectHandler(**net_device)
        print(ssh_conn.find_prompt())

        source_file = "my_file.txt"
        dest_file = "my_file.txt"

        transfer_dict = file_transfer(
            ssh_conn,
            source_file=source_file,
            dest_file=dest_file,
            file_system=file_system,
            direction='put',
            overwrite_file=False,
        )

        md5_check = transfer_dict['file_verified']
        file_exists = transfer_dict['file_exists']

        if md5_check and file_exists:
            print("File successfully transferred to: {host}".format(**net_device))
        else:
            print("Failure on SCP: {host} !!!".format(**net_device))
        print()


if __name__ == "__main__":
    main()
