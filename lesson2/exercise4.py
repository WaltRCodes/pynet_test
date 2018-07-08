from __future__ import print_function, unicode_literals
import getpass
import snmp_helper


def main():
    ip_address1 = '184.105.247.70'
    ip_address2 = '184.105.247.71'
    com_string = 'galileo'
    
    pynet_rtr1 = (ip_address1, com_string, 161)
    pynet_rtr2 = (ip_address2, com_string, 161)

    for a_device in (pynet_rtr1, pynet_rtr2):
        for my_oid in ('1.3.6.1.2.1.1.1.0', '1.3.6.1.2.1.1.5.0'):
            snmp_data = snmp_helper.snmp_get_oid(a_device, oid=my_oid)
            output = snmp_helper.snmp_extract(snmp_data)
            print(output)

if __name__ == "__main__":
    main()
