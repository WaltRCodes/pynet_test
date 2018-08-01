from __future__ import print_function, unicode_literals
import jinja2

ospf_template = """
router ospf {{ PID }}
 network {{ network }} {{ netmask }} area {{ area }}
"""

variables = {
    'PID': 40,
    'network': '10.220.88.0',
    'netmask': '0.0.0.255',
    'area': 0,
}

template = jinja2.Template(ospf_template)
output = template.render(**variables)
print(output)
