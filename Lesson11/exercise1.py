from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler, file_transfer


def device_dictionary(hostname):
    return {
        'device_type': 'arista_eos',
        'host': hostname,
        'username': 'pyclass',
        'password': '88newclass',
        'file_system': "/mnt/flash",
    }


def main():
    hostnames = [
        'arista1.twb-tech.com',
        'arista2.twb-tech.com',
        'arista3.twb-tech.com',
        'arista4.twb-tech.com',
    ]

    for host in hostnames:
        net_device = device_dictionary(host)
        file_system = net_device.pop('file_system')
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
