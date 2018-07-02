from __future__ import print_function, unicode_literals
import paramiko
import time
from getpass import getpass

MAX_BUFFER = 65535

def clearbuff(remote_conn):
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER).decode('utf-8', 'ignore')
def disablepag(remote_conn, cmd='terminal length 0'):
    cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(1)
    clearbuff(remote_conn)
def push_command(remote_conn, cmd='', delay=1):
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER).decode('utf-8', 'ignore')
    else:
        return ''


def main():

    try:
        ip_addr = raw_input("Enter IP address: ")
    except NameError:
        ip_addr = input("Enter IP address: ")
    username = 'pyclass'
    password = '88newclass'
    port = 22

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    time.sleep(1)
    clearbuff(remote_conn)
    disablepag(remote_conn)

    nextoutput = push_command(remote_conn, cmd='sh ver')
    print('\n')
    print(nextoutput)
    print('\n')


if __name__ == "__main__":
    main()
