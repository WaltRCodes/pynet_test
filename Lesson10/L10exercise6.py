from __future__ import print_function, unicode_literals
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

def main():

    juniper_srx = {
        "host": "184.105.247.76",
        "user": "pyclass",
        "password": "88newclass"
    }

    print("\n\nConnecting to Juniper SRX...\n")
    a_device = Device(**juniper_srx)
    a_device.open()

    cfg = Config(a_device)

    print("Setting hostname using set notation")
    cfg.load("set system host-name thisismytestname", format="set", merge=True)

    print("Current config differences: ")
    print(cfg.diff())

    print("Performing rollback")
    cfg.rollback(0)

    print("\nSetting hostname using {} notation (external file)")
    cfg.load(path="load_hostname.conf", format="text", merge=True)

    print("Current config differences: ")
    print(cfg.diff())

    print("Performing commit")
    cfg.commit()

    print("\nSetting hostname using XML (external file)")
    cfg.load(path="load_hostname.xml", format="xml", merge=True)

    print("Current config differences: ")
    print(cfg.diff())

    print("Performing commit")
    cfg.commit()
    print()


if __name__ == "__main__":
    main()
