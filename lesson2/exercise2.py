from __future__ import print_function, unicode_literals

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 5

def utf_coversion(data):
    if sys.version_info[0] >= 3:
        if isinstance(data, type(u'')):
            return data.encode('utf-8')
        elif isinstance(data,type(b'')):
            return data
    else:
        if isinstance(data, type(u'')):
            return data.encode('utf-8')
        elif isinstance(data, type(str(''))):
            return data
    msg = "Invalid value: {}".format(data)
    raise ValueError(msg)

def write_ch(remote_conn,data):
    remote_conn.write(utf_coversion(data))

def read_ch(remote_conn):
    return remote_conn.read_very_eager().decode('utf-8','ignore')
def telnet_connect(ip_address):
    try:
        return telnetlib.Telnet(ip_address,TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")

def login(remote_conn, username, password):
    output = remote_conn.read_until(b"sername:",TELNET_TIMEOUT).decode('utf-8', 'ignore')
    write_ch(remote_conn, username + '\n')
    output += remote_conn.read_until(b"ssword:", TELNET_TIMEOUT).decode('utf-8', 'ignore')
    write_ch(remote_conn, password + '\n')
    return output

def disable_paging(remote_conn, paging_cmd='terminal length 0'):
    return send_command(remote_conn, paging_cmd)

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    write_ch(remote_conn, cmd + '\n')
    time.sleep(1)
    return read_ch(remote_conn)

def main():
    try:
        ip_address = raw_input("IP address: ")
    except NameError:
        ip_address = input("IP address: ")
    ip_address = ip_address.strip()
    username = 'pyclass'
    password = getpass.getpass()

    remote_conn = telnet_connect(ip_address)
    output = login(remote_conn, username, password)

    time.sleep(1)
    read_ch(remote_conn)
    disable_paging(remote_conn)

    output = send_command(remote_conn, 'sh ip int brief')
    print(output)

    remote_conn.close()

if __name__ == "__main__":
    main()
