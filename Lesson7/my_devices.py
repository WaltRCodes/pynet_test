std_pwd = "88newclass"
pynet_rtr1 = {
    'device_type': 'ios',
    'hostname': '184.105.247.70',
    'username': 'pyclass',
    'password': std_pwd,
    'optional_args': {},
}
pynet_rtr2 = {
    'device_type': 'ios',
    'hostname': '184.105.247.71',
    'username': 'pyclass',
    'password': std_pwd,
    'optional_args': {},
}
pynet_sw1 = {
    'device_type': 'eos',
    'hostname': '184.105.247.72',
    'username': 'pyclass',
    'password': std_pwd,
    'optional_args': {},
}
pynet_sw2 = {
    'device_type': 'eos',
    'hostname': '184.105.247.73',
    'username': 'pyclass',
    'password': std_pwd,
    'optional_args': {},
}
juniper_srx = {
    'device_type': 'junos',
    'hostname': '184.105.247.76',
    'username': 'pyclass',
    'password': std_pwd,
    'optional_args': {},
}
nxos1 = {
    'device_type': 'nxos',
    'hostname': 'nxos1.twb-tech.com',
    'username': 'pyclass',
    'password': std_pwd,
    'optional_args': {'port': 8443},
}
device_list = [
        pynet_rtr1,
        pynet_rtr2,
        pynet_sw1,
        pynet_sw2,
        juniper_srx,
        nxos1,
]
