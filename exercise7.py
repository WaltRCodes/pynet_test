from __future__ import unicode_literals, print_function
import yaml
import json
from pprint import pprint

def output_format(this_list,arg):
    print('---------------------')
    print(arg)
    pprint(this_list)







def main():
    ytest = 'test.yml'
    jtest = 'test.json'
    
    with open(ytest) as f:
        ylist = yaml.load(f)
    with open (jtest) as f:
        jlist = json.load( f)
    output_format(ylist, 'YAML')
    output_format(jlist, 'JSON')
    print('\n')


if __name__ == "__main__":
    main()
