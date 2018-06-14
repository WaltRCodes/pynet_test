from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse
import re

def main():
    text_file = 'cisco_ipsec.txt'

    config = CiscoConfParse(text_file)
    maps = config.find_objects_wo_child(parentspec=r'crypto map CRYPTO',childspec=r'AES')

    for i in maps:
        print(i.text)
        for x in i.children:
            print(x.text)
            if 'transform' in x.text:
                found = re.search(r"set transform-set (.*)$", x.text)
        print("{} | {}".format(i.text.strip(),found.group(1)))
        
   

if __name__ == "__main__":
    main()
