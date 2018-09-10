from __future__ import print_function, unicode_literals
from lxml import etree
from jnpr.junos import Device


def main():
    juniper_srx = {
        "host": "184.105.247.76",
        "user": "pyclass",
        "password": "88newclass"
    }

    print("\n\nConnecting to Juniper SRX...\n")
    a_device = Device(**juniper_srx)
    a_device.open()

    show_version = a_device.rpc.get_software_information()
    print(etree.tostring(show_version, pretty_print=True).decode())
    model = show_version.xpath("product-model")[0].text
    print("SRX Model: {}".format(model))
    print()


if __name__ == "__main__":
    main()
