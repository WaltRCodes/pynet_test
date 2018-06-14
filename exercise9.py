from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse


def main():
    text_file = 'cisco_ipsec.txt'

    config = CiscoConfParse(text_file)
    maps = config.find_objects_w_child(parentspec=r'crypto map CRYPTO',childspec=r'pfs group2')

    for i in maps:
        print(i.text)
        
    print('\n')




if __name__ == "__main__":
    main()
