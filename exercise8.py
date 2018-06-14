from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse


def main():
    text_file = 'cisco_ipsec.txt'

    config = CiscoConfParse(text_file)
    maps = config.find_objects(r"^crypto map CRYPTO")

    for i in maps:
        print(i.text)
        for x in i.children:
            print(x.text)
    print('\n')




if __name__ == "__main__":
    main()
