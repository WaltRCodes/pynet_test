from __future__ import print_function, unicode_literals
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

device_vars = {
    'snmp_location': 'San Francisco, CA',
    'snmp_contact': 'Isaac Newton',
    'snmp_community': 'foo',
}

file = 'arista_template.j2'
template = env.get_template(file)
print(template.render(device_vars))
