from __future__ import unicode_literals, print_function
from lxml import etree
from pprint import pprint

with open('show_arp.xml') as f:
    arp = etree.fromstring(f.read())

print(etree.tostring(arp, pretty_print=True).decode())

xpath_arp = '//arp-table-entry'
arp_entries = arp.xpath(xpath_arp)

mac_xpath = 'mac-address'
ip_xpath = 'ip-address'
intf_xpath = 'interface-name'

arp_dict = {}
for arp_entry in arp_entries:
    mac_address = arp_entry.xpath(mac_xpath)[0].text
    ip_address = arp_entry.xpath(ip_xpath)[0].text
    intf = arp_entry.xpath(intf_xpath)[0].text
    arp_dict[ip_address] = {
        'mac_addr': mac_address,
        'intf': intf
    }


pprint(arp_dict)
print()
