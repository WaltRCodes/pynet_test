from __future__ import print_function, unicode_literals
import jinja2

file = 'ospf_config_for.j2'
with open(file) as f:
    ospf_template = f.read()

ospf_networks = [
    {
        'network': '10.220.88.0',
        'wildcard': '0.0.0.255',
        'area': 0,
    },
    {
        'network': '172.31.255.28',
        'wildcard': '0.0.0.0',
        'area': 1,
    },
]

ospf_vars = {
    'process_id': 40,
    'ospf_networks': ospf_networks,
    'loopback0_addr': '172.31.255.1',
    'loopback0_mask': '255.255.255.255',
}

template = jinja2.Template(ospf_template)
output = template.render(**ospf_vars)
print(output)
