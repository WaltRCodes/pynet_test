from __future__ import print_function, unicode_literals
import pexpect
import time
from getpass import getpass


def login(ssh_conn):
    password = '88newclass'
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')


def find_prompt(ssh_conn):
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip()


def disablepag(ssh_conn, pattern='#', cmd='terminal length 0'):
    ssh_conn.sendline(cmd)
    ssh_conn.expect(pattern)


def main():
    try:
        ip_addr = raw_input("Enter IP address: ")
    except NameError:
        ip_addr = input("Enter IP address: ")
    username = 'pyclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3

    login(ssh_conn)
    prompt = find_prompt(ssh_conn)
    disablepag(ssh_conn, prompt)

    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')

    ssh_conn.sendline('logging buffer 9000')
    ssh_conn.expect('#')

    ssh_conn.sendline('end')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show run | inc logging buffer')
    ssh_conn.expect(prompt)

    print('\n')
    print(ssh_conn.before.decode('utf-8', 'ignore'))
    print('\n')


if __name__ == "__main__":
    main()
