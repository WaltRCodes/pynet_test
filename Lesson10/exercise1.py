from __future__ import unicode_literals, print_function
from lxml import etree
from pprint import pprint

with open('show_lldp.xml') as f:
    lldp = etree.fromstring(f.read())

print(etree.tostring(lldp, pretty_print=True).decode())

lldp_child = lldp.getchildren()[0]
print(lldp_child.tag)

for child in lldp_child:
    if child.tag == 'lldp-local-interface':
        local_intf = child.text
    elif child.tag == 'lldp-remote-system-name':
        remote_sys_name = child.text
    elif child.tag == 'lldp-remote-port-description':
        remote_port = child.text

lldp_dict = {
    local_intf: {
        'remote_sys_name': remote_sys_name,
        'remote_port': remote_port,
    }
}


pprint(lldp_dict)
print('\n\n')
