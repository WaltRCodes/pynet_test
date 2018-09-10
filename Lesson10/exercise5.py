from __future__ import print_function, unicode_literals

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable


def main():

    juniper_srx = {
        "host": "184.105.247.76",
        "user": "pyclass",
        "password": "88newclass"
    }

    print("\n\nConnecting to Juniper SRX...\n")
    a_device = Device(**juniper_srx)
    a_device.open()

    routes = RouteTable(a_device)
    routes.get()

    print("\nJuniper SRX Routing Table: ")
    for a_route, route_attr in routes.items():
        print("\n" + a_route)
        for attr_desc, attr_value in route_attr:
            print("  {} {}".format(attr_desc, attr_value))

    print("\n")


if __name__ == "__main__":
    main()
